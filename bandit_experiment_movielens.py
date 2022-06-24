import argparse
import pandas as pd
import time
import numpy as np
from heavy_tail_observations import BothSideWeibullNoise, BothSideParetoNoise, BothSideFrechetNoise
from heavy_tail_lin_bandit import MENU, TOFU, SupHvyLinBandit

parser = argparse.ArgumentParser(description="Run experiments on various robust mean estimators under heavy tailed noise")
parser.add_argument('--optim_type', metavar='opt', type=str, default='proof', choices=['menu', 'tofu', 'proof', 'supbtc', 'supbmm'], help='Optimizer')
parser.add_argument('--moment', metavar='p', type=float, default=1.9, help='A maximum bounded moment')
parser.add_argument('--seed', metavar='i', type=int, default=0, help='A random seed')
parser.add_argument('--samples', metavar='n', type=int, default=1000, help='Samples')
parser.add_argument('--norm', metavar='nrm', type=float, default=1., help='Input Norm')

args = parser.parse_args()
seed = args.seed
p = args.moment
T = args.samples
S = args.norm
optim_type = args.optim_type

#import of review data
cols = ["user id","item id","rating","timestamp"]
#encoding using ISO-8859-1 is used because utf-8 does not support all the characters in movie names
df_data = pd.read_csv("ml-100k/u.data",sep="\t",names=cols,header=None,encoding="ISO-8859-1")
# df_data.head()

#import of moviedata
cols = ["movie id","movie title","release date","video release date","IMDb URL","unknown",
        "Action","Adventure","Animation","Childrens","Comedy","Crime","Documentary",
        "Drama","Fantasy","Film-Noir","Horror","Musical","Mystery","Romance","Sci-Fi",
        "Thriller","War","Western"]

df_movie = pd.read_csv("ml-100k/u.item",sep="|",names=cols,header=None,encoding="ISO-8859-1")
# df_movie.head()

#import of user data
cols = ["user id","age","gender","occupation","zip code"]
df_user = pd.read_csv("ml-100k/u.user",sep="|",names=cols,header=None,encoding="ISO-8859-1")
# df_user.head()

#frequency binning the ages into age groups as it will be easier for future analysis
df_user['age_group'] = pd.qcut(df_user['age'],q=10,precision=0)

#join all three dataframes

df = pd.merge(pd.merge(df_data,
                  df_user[["user id",
                           "age_group",
                           "gender",
                           "occupation"]],
                  on='user id',
                  how='left'),
              df_movie,
              left_on = 'item id',
              right_on = 'movie id',
              how ='left')
# df.head()

#drop unneccessary features
df.drop(["movie id",
        "movie title",
        "release date",
        "video release date",
        "IMDb URL",
        "unknown",
        "user id",
        "item id",
        "timestamp"],axis=1, inplace=True)
# df.head()

# check for null values
df.isnull().sum()

#categorize age_group, gender and occupation using 1-hot encoder
df['age_group'] = pd.Categorical(df['age_group'])
df['gender'] = pd.Categorical(df['gender'])
df['occupation'] = pd.Categorical(df['occupation'])

age_group_dummies = pd.get_dummies(df['age_group'])
gender_dummies = pd.get_dummies(df['gender'])
occupation_dummies = pd.get_dummies(df['occupation'])

df = pd.concat([df,
                age_group_dummies,
                gender_dummies,
                occupation_dummies], axis=1)

df.drop(['age_group',
        'gender',
        'occupation'], axis=1, inplace=True)

np.random.seed(seed)
y = df.rating.to_numpy()
X = df.drop('rating',axis=1).to_numpy()
dim = X.shape[1]
total_samples = len(y)

K = int(total_samples/T)

D = np.reshape(X, (T,K,dim))
R = np.reshape(y, (T,K))

indices = np.random.permutation(T)
D = D[indices]
R = R[indices]

get_mean = lambda x, y: R[y]
get_observation = lambda x, y, z: R[y][z]

optim_names = []
optim_params = []
optims = []
if optim_type == 'menu':
    lamb_list = 10**np.linspace(-3.,2.,10)
    c_list = 10**np.linspace(-4.,1.,10)
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
        
filename = 'bandit_movielens_results/p{:.2f}-dim{:d}-size{:d}-action{:d}-{:}-seed{:d}.npy'.format(p,dim,T,K,optim_type,seed)
with open(filename,'wb') as f:
    np.savez(f, 
             p=p,
             T=T,
             K=K,
             optim_type=optim_type,
             optim_params=optim_params,
             optim_names=optim_names,
             error_list=error_list,
             time_list=time_list
            )
    print('Data saved at {}'.format(filename))
