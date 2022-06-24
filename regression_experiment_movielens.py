import argparse
import pandas as pd
import time
import numpy as np
from sklearn.model_selection import train_test_split

from heavy_tail_observations import BothSideWeibullNoise, BothSideParetoNoise, BothSideFrechetNoise
from heavy_tail_regressions import catoni_lin_reg, mom_lin_reg, pro, reg_lin_reg, trunc_lin_reg, trunc_reg

parser = argparse.ArgumentParser(description="Run experiments on various robust mean estimators under heavy tailed noise")
parser.add_argument('--dataset', metavar='data', type=str, default='movielens', choices=['movielens', 'sandp500_AAPL']) 
parser.add_argument('--optim_type', metavar='opt', type=str, default='pro', choices=['catoni', 'mom', 'pro', 'reg', 'trunc_lin', 'trunc'], help='Optimizer')
parser.add_argument('--seed', metavar='i', type=int, default=0, help='A random seed')
parser.add_argument('--samples', metavar='n', type=int, default=1000, help='Samples')

args = parser.parse_args()
seed = args.seed
n = args.samples
optim_type = args.optim_type
p = 1.5

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
y = df.rating.to_numpy()[:n]
x = df.drop('rating',axis=1).to_numpy()[:n]

# split data into 70% (training set) and 30% (testing set)
x_data,x_list,y_data,mean_list = train_test_split(x,y,test_size=0.3)

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
    beta_list = 10**np.linspace(-4.,1.,10)
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
for opt_idx, (optim, optim_param, optim_name)  in enumerate(zip(optims,optim_params,optim_names)):
    start = time.time()
    est_mean_list, w_hat = optim(*(x_data,y_data,x_list,p),**optim_param)
    end = time.time()
    error = np.mean(np.abs(est_mean_list - mean_list))
    error_list[opt_idx].append(error)
    time_list[opt_idx].append(end-start)
        
filename = 'estimation_movielens_results/movielens-size{:d}-{:}-seed{:d}.npy'.format(n,optim_type,seed)
with open(filename,'wb') as f:
    np.savez(f, 
             n=n,
             optim_type=optim_type,
             optim_params=optim_params,
             optim_names=optim_names,
             error_list=error_list,
             time_list=time_list
            )
    print('Data saved at {}'.format(filename))
