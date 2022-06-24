import argparse
import time
import numpy as np

from heavy_tail_observations import BothSideWeibullNoise, BothSideParetoNoise, BothSideFrechetNoise
from heavy_tail_regressions import catoni_lin_reg, mom_lin_reg, pro, reg_lin_reg, trunc_lin_reg, trunc_reg

parser = argparse.ArgumentParser(description="Run experiments on various robust mean estimators under heavy tailed noise")
parser.add_argument('--noise', metavar='dist', type=str, default='weibull', choices=['weibull', 'frechet', 'pareto'], help='A type of noise')
parser.add_argument('--optim_type', metavar='opt', type=str, default='pro', choices=['catoni', 'mom', 'pro', 'reg', 'trunc_lin', 'trunc'], help='Optimizer')
parser.add_argument('--moment', metavar='p', type=float, default=1.9, help='A maximum bounded moment')
parser.add_argument('--scale', metavar='s', type=float, default=1.0, help='Scale of noise')
parser.add_argument('--seed', metavar='i', type=int, default=0, help='A random seed')
parser.add_argument('--samples', metavar='n', type=int, default=1000, help='Samples')
parser.add_argument('--dimension', metavar='d', type=int, default=5, help='Input Dimension')
parser.add_argument('--steps', metavar='t', type=int, default=100, help='Steps')

args = parser.parse_args()
seed = args.seed
noise_type = args.noise
scale = args.scale
p = args.moment
n = args.samples
dim = args.dimension
optim_type = args.optim_type

weight = np.random.randn(dim+1)
weight = weight/np.sqrt(weight.dot(weight))
    
if noise_type == 'weibull':
    weibull_noise = BothSideWeibullNoise(alpha=p+0.1,scale=scale,mean=0.,p=p)
    get_observation = lambda x: x.dot(weight) + weibull_noise.sample()
elif noise_type == 'pareto':
    pareto_noise = BothSideParetoNoise(alpha=p+0.1,scale=scale,mean=0.,p=p)
    get_observation = lambda x: x.dot(weight) + pareto_noise.sample()
elif noise_type == 'frechet':
    frechet_noise = BothSideFrechetNoise(alpha=p+0.1,scale=scale,mean=0.,p=p)
    get_observation = lambda x: x.dot(weight) + frechet_noise.sample()
    
np.random.seed(seed)
x_list = 20.*np.random.randn(100,dim+1)
mean_list = x_list.dot(weight)

x_data = 5.*np.random.randn(n,dim+1)
x_data[:,0] = 1.
y_data = [get_observation(x) for x in x_data]

optim_names = []
optim_params = []
optims = []
if optim_type == 'catoni':
    beta_list = 10**np.linspace(-3.,2.,10)
    for i in range(len(beta_list)):
        optim_names.append("{:}(beta:{:f})".format(optim_type, beta_list[i]))
        optim_params.append({'beta':beta_list[i]})
        optims.append(catoni_lin_reg)
elif optim_type == 'mom':
    lam_list = 10**np.linspace(-3.,2.,10)
    k_list = np.linspace(1,10,10)
    for i in range(len(lam_list)):
        for j in range(len(k_list)):
            optim_names.append("{:}(lam:{:f},K:{:d})".format(optim_type, lam_list[i], int(k_list[j])))
            optim_params.append({'lam':lam_list[i],'k':int(k_list[j])})
            optims.append(mom_lin_reg)
elif optim_type == 'pro':
    lam_list = 10**np.linspace(-3.,2.,10)
    beta_list = 10**np.linspace(-3.,2.,10)
    for i in range(len(lam_list)):
        for j in range(len(beta_list)):
            optim_names.append("{:}(lam:{:f},beta:{:f})".format(optim_type, lam_list[i], beta_list[j]))
            optim_params.append({'lam':lam_list[i],'beta':beta_list[j]})
            optims.append(pro)
elif optim_type == 'reg':
    lam_list = 10**np.linspace(-3.,2.,10)
    for i in range(len(lam_list)):
        optim_names.append("{:}(lam:{:f})".format(optim_type, lam_list[i]))
        optim_params.append({'lam':lam_list[i]})
        optims.append(reg_lin_reg)
elif optim_type == 'trunc_lin':
    lam_list = 10**np.linspace(-3.,2.,10)
    beta_list = 10**np.linspace(-3.,2.,10)
    for i in range(len(lam_list)):
        for j in range(len(beta_list)):
            optim_names.append("{:}(lam:{:f},beta:{:f})".format(optim_type, lam_list[i], beta_list[j]))
            optim_params.append({'lam':lam_list[i],'beta':beta_list[j]})
            optims.append(trunc_lin_reg)
elif optim_type == 'trunc':
    lam_list = 10**np.linspace(-3.,2.,10)
    for i in range(len(lam_list)):
        optim_names.append("{:}".format(optim_type))
        optim_params.append({'lam':lam_list[i]})
        optims.append(trunc_reg)
        
error_list = [[] for _ in range(len(optims))]
time_list = [[] for _ in range(len(optims))]
increments = n//10
for step in range(10):
    samples = increments*(step+1)
    for opt_idx, (optim, optim_param, optim_name)  in enumerate(zip(optims,optim_params,optim_names)):
        start = time.time()
        est_mean_list, w_hat = optim(*(x_data[:samples],y_data[:samples],x_list,p),**optim_param)
        end = time.time()
        error = np.mean(np.abs(est_mean_list - mean_list))
        error_list[opt_idx].append(error)
        time_list[opt_idx].append(end-start)
        
filename = 'estimation_results/{:}-p{:.2f}-s{:.2f}-dim{:d}-size{:d}-{:}-seed{:d}.npy'.format(noise_type,p,scale,dim,samples,optim_type,seed)
with open(filename,'wb') as f:
    np.savez(f, 
             p=p,
             scale=scale,
             n=n,
             weight=weight,
             optim_type=optim_type,
             optim_params=optim_params,
             optim_names=optim_names,
             error_list=error_list,
             time_list=time_list
            )
    print('Data saved at {}'.format(filename))
