import numpy as np
from scipy.stats import beta

class Population(object):
    
    
    def __init__(self):
        self._true_mean = 0.7
        self._true_precision = 20
        self._distribution =  beta(self._true_mean*self._true_precision,
                                   (1-self._true_mean)*self._true_precision,
                                   loc = 0, 
                                   scale = 100)
        
        self.pop_mean = self._distribution.mean()
        self.pop_sd = self._distribution.std()
        
    def sample(self, size):
        
        samples = self._distribution.rvs(size=size)
        
        return np.sort(samples)