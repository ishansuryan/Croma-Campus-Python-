from sklearn.base import BaseEstimator,TransformerMixin
import numpy as np

class converter(BaseEstimator, TransformerMixin):        
    def fit(self,x,y=None):
        return self
        
    def transform(self, x,y=None):
        data_num = np.array(x)[:,:8]
        return np.array(data_num,dtype = np.float32)

class encode (BaseEstimator,TransformerMixin): 
    def fit(self, x, y =None):
        return self
    def transform(self, x,y=None):
        data_cat = np.array(x)[:,-1]
        return data_cat.reshape(-1,1)

# if __name__ != '__main__':
#     import numpy as np

# c = converter()
# l = np.array(([1,2,3,4,5,6,7,8,"8"],[1,2,3,4,5,6,7,8,'j']))
# print(c.fit_transform(l))