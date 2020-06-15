import pandas as pd 
import numpy as np


# Panda Series is an One Dimensional Container Similar to Python List
s = pd.Series()
print(s)

data = np.array(['a','b','c','d'])
s = pd.Series(data)

s1 = pd.Series(data,index=['100','101','102','103'])

print(s)
print(s1)

# Creating a series from a dict

data = {'a': 0., 'b' : 1., 'c' : 2}
s2 = pd.Series(data,index=['b','c','d','a'])
print(s2)