import numpy as np
from scipy.stats import invweibull
from scipy.special import gamma

class BothSideWeibullNoise():
    def __init__(self,alpha=1.6, scale=1., mean=0., p=1.5):
        self.alpha = alpha
        self.scale = scale
        self.mean = mean
        self.p = p
        self.nu_p = (scale**p)*gamma(1.+p/alpha)

    def sample(self):
        if np.random.uniform() > 0.5:
            return self.mean + self.scale*(np.random.weibull(self.alpha)-gamma(1.+1./self.alpha))
        else:
            return self.mean - self.scale*(np.random.weibull(self.alpha)-gamma(1.+1./self.alpha))

        
class BothSideParetoNoise():
    def __init__(self,alpha=1.6, scale=1., mean=0., p=1.5):
        self.alpha = alpha
        self.scale = scale
        self.mean = mean
        self.p = p
        self.nu_p = (scale**p)*alpha/(alpha-p)
        
    def sample(self):
        if np.random.uniform() > 0.5:
            return self.scale*(np.random.pareto(self.alpha)-self.alpha/(self.alpha-1)) + self.mean
        else:
            return -self.scale*(np.random.pareto(self.alpha)-self.alpha/(self.alpha-1)) + self.mean
        
        
class BothSideFrechetNoise():
    def __init__(self,alpha=1.6, scale=1., mean=0., p=1.5):
        self.alpha = alpha
        self.scale = scale
        self.mean = mean
        self.p = p
        self.nu_p = (scale**p)*gamma(1.-p/alpha)

    def sample(self):
        if np.random.uniform() > 0.5:
            return self.scale*(invweibull.rvs(self.alpha,scale=1.)-(self.alpha/(self.alpha+1))**(1/self.alpha)) + self.mean
        else:
            return -self.scale*(invweibull.rvs(self.alpha,scale=1.)-(self.alpha/(self.alpha+1))**(1/self.alpha)) + self.mean