# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 14:10:56 2018 by Goldie Sahni
"""

import pandas
pandas.__version__
import pandas as pd
pd?
import numpy as np
data=pd.Series([0.25,0.5,0.75,1.0])
data
data.values
data.index
data[1]
data[2]
data[1:3]
data=pd.Series([0.25,0.5,0.75,1.0],index=['a','b','c','d'])
data
data['b']
dict1 = {'b':23,'d':45,'h':67}
s1=pd.Series(dict1)
s1
pd.Series(5,index=[100,200,300])
population=[100,200,300]
area=[10,20,30]
states=pd.DataFrame({'population':population,'area':area})
states
states.columns
rollno = [1,2,3]
names=['A','B','C']
df1 = pd.DataFrame(rollno,columns=['rollno'])
sdata=pd.DataFrame({'rollno':rollno,'sname':names})
sdata
sdata2=pd.DataFrame(list(zip(rollno,names)))
sdata2
sdata2.columns=['rollno','names']
sdata2
pd.DataFrame(np.random.rand(3,2),columns=['foo','bar'],
             index=['a','b','c'])
ind = pd.Index([2,3,5,7,11])
ind
ind[1]
ind[::2]
list(ind[::2])
inda=pd.Index([1,3,5,7,9])
indb=pd.Index([2,3,6,7,8])
inda & indb
data.iloc[1]
data.loc['a']
data.values[0]
df1.values[0]
sdata2
