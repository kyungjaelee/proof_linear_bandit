import argparse
import time
import numpy as np
from heavy_tail_observations import BothSideWeibullNoise, BothSideParetoNoise, BothSideFrechetNoise
from heavy_tail_lin_bandit import MENU, TOFU, SupHvyLinBandit

parser = argparse.ArgumentParser(description="Run experiments on various robust mean estimators under heavy tailed noise")
parser.add_argument('--noise', metavar='dist', type=str, default='weibull', choices=['weibull', 'frechet', 'pareto'], help='A type of noise')
parser.add_argument('--optim_type', metavar='opt', type=str, default='proof', choices=['menu', 'tofu', 'proof', 'supbtc', 'supbmm'], help='Optimizer')
parser.add_argument('--moment', metavar='p', type=float, default=1.9, help='A maximum bounded moment')
parser.add_argument('--scale', metavar='s', type=float, default=1.0, help='Scale of noise')
parser.add_argument('--seed', metavar='i', type=int, default=0, help='A random seed')
parser.add_argument('--samples', metavar='n', type=int, default=1000, help='Samples')
parser.add_argument('--actions', metavar='K', type=int, default=10, help='Actions')
parser.add_argument('--dimension', metavar='d', type=int, default=5, help='Input Dimension')
parser.add_argument('--norm', metavar='nrm', type=float, default=1., help='Input Norm')

args = parser.parse_args()
seed = args.seed
noise_type = args.noise
scale = args.scale
p = args.moment
dim = args.dimension
T = args.samples
S = args.norm
optim_type = args.optim_type
K = args.actions
mean=0.

np.random.seed(seed)
weight = np.random.randn(dim)
weight = S*weight/np.sqrt(weight.dot(weight))
    
get_mean = lambda x, y: x.dot(weight)
if noise_type == 'weibull':
    weibull_noise = BothSideWeibullNoise(alpha=p+0.1,scale=scale,mean=mean,p=p)
    get_observation = lambda x, y, z: x.dot(weight) + weibull_noise.sample()
elif noise_type == 'pareto':
    pareto_noise = BothSideParetoNoise(alpha=p+0.1,scale=scale,mean=mean,p=p)
    get_observation = lambda x, y, z: x.dot(weight) + pareto_noise.sample()
elif noise_type == 'frechet':
    frechet_noise = BothSideFrechetNoise(alpha=p+0.1,scale=scale,mean=mean,p=p)
    get_observation = lambda x, y, z: x.dot(weight) + frechet_noise.sample()
    
D = np.random.randn(T,K,dim)

optim_names = []
optim_params = []
optims = []
if optim_type == 'menu':
    lamb_list = 10**np.linspace(-3.,2.,10)
    c_list = 10**np.linspace(-2.,3.,10)
    for i in range(len(lamb_list)):
        for j in range(len(c_list)):
            optim_names.append("{:}(lamb:{:f},c:{:f})".format(optim_type, lamb_list[i], c_list[j]))
            optim_params.append({'S':S, 'p':p, 'delta': 1e-3, 'lamb':lamb_list[i], 'c': c_list[j]})
            optims.append(MENU)
elif optim_type == 'tofu':
    lamb_list = 10**np.linspace(-3.,2.,10)
    b_list = 10**np.linspace(-4.,1.,10)
    for i in range(len(lamb_list)):
        for j in range(len(b_list)):
            optim_names.append("{:}(lamb:{:f},b:{:f})".format(optim_type, lamb_list[i], b_list[j]))
            optim_params.append({'S':S, 'p':p, 'delta': 1e-3, 'lamb':lamb_list[i], 'b': b_list[j]})
            optims.append(TOFU)
elif optim_type == 'supbtc':
    lamb_list = 10**np.linspace(-3.,2.,10)
    nu_list = 10**np.linspace(-4.,1.,10)
    for i in range(len(lamb_list)):
        for j in range(len(nu_list)):
            optim_names.append("{:}(lamb:{:f},nu:{:f})".format(optim_type, lamb_list[i], nu_list[j]))
            optim_params.append({'S':S, 'p':p, 'method':'btc', 'delta': 1e-3, 'lamb':lamb_list[i], 'nu': nu_list[j]})
            optims.append(SupHvyLinBandit)
elif optim_type == 'supbmm':
    lamb_list = 10**np.linspace(-3.,2.,10)
    nu_list = 10**np.linspace(-4.,1.,10)
    for i in range(len(lamb_list)):
        for j in range(len(nu_list)):
            optim_names.append("{:}(lamb:{:f},nu:{:f})".format(optim_type, lamb_list[i], nu_list[j]))
            optim_params.append({'S':S, 'p':p, 'method':'bmm', 'delta': 1e-3, 'lamb':lamb_list[i], 'nu': nu_list[j]})
            optims.append(SupHvyLinBandit)
elif optim_type == 'proof':
    lamb_list = 10**np.linspace(-3.,2.,10)
    nu_list = 10**np.linspace(-4.,1.,10)
    for i in range(len(lamb_list)):
        for j in range(len(nu_list)):
            optim_names.append("{:}(lamb:{:f},nu:{:f})".format(optim_type, lamb_list[i], nu_list[j]))
            optim_params.append({'S':S, 'p':p, 'method':'proof', 'delta': 1e-3, 'lamb':lamb_list[i], 'nu': nu_list[j]})
            optims.append(SupHvyLinBandit)
        
error_list = [[] for _ in range(len(optims))]
time_list = [[] for _ in range(len(optims))]
for opt_idx, (optim, optim_param, optim_name)  in enumerate(zip(optims,optim_params,optim_names)):
    start = time.time()
    err_list, _ = optim(*(D, get_mean, get_observation),**optim_param)
    end = time.time()
    error_list[opt_idx].append(err_list)
    time_list[opt_idx].append(end-start)
        
filename = 'bandit_results/{:}-p{:.2f}-s{:.2f}-dim{:d}-size{:d}-action{:d}-{:}-seed{:d}.npy'.format(noise_type,p,scale,dim,T,K,optim_type,seed)
with open(filename,'wb') as f:
    np.savez(f, 
             p=p,
             scale=scale,
             T=T,
             K=K,
             weight=weight,
             optim_type=optim_type,
             optim_params=optim_params,
             optim_names=optim_names,
             error_list=error_list,
             time_list=time_list
            )
    print('Data saved at {}'.format(filename))
