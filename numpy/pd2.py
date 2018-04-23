# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 13:39:19 2018 by Goldie Sahni
"""

import numpy as np
import pandas as pd
S1 = pd.Series([12,34,67,78,76])
S1.index
S1
s = pd.Series([3,7,4,4,0.3],['a','b','c','d','e'])
s
df = pd.DataFrame(np.arange(9).reshape(3,3),['b','a','c'],['Paris','Berlin','Madrid'])
df
s['b']
s[1:4]
s['a':'c']
df.head()
df[1:2]
df['Paris']
df[0,1]
df[0]
df
df[0:1]
df[df['Paris']>1]
df.Berlin[df['Berlin']>1]=0
df
df.ix['a','Berlin']
df.ix[['b','c'],['Berlin','Madrid']]
s
s.drop('d')
s2 = pd.Series([0,1,2],['a','c','f'])
s2
s+s2
s-s2
s.add(s2,fill_value=0)
df2 = pd.DataFrame(np.arange(12).reshape(4,3),['b','e','c','a'],['Paris','Lisbonne','Madrid'])
df2
df+df2
df.add(df2,fill_value=0)
df1 = pd.DataFrame({'data1':[0,1,2,3,4,5,6],'keyleft':['b','b','a','c','a','a','b']})
df1
df2 = pd.DataFrame({'data2':np.arange(3),'key':['a','b','d']})
df2
pd.merge(df1,df2,left_on='keyleft',right_on='key',how='inner')
pd.merge(df1,df2,left_on='keyleft',right_on='key',how='outer')
pd.merge(df1,df2)
left1 = pd.DataFrame({'key':['a','b','a','a','b','c'],'data1':np.arange(6)})
right1 = pd.DataFrame({'data2':np.arange(5),'key':['a','b','a','b','d']})
pd.merge(left1,right1,on='key',how='left')
s.rank
s.rank()
s.rank(method='first')
df.rank()
s.sort_index()
df.max()
df
df+df.max()
import math
f=lambda x: math.sqrt(x)
df.applymap(f)
df.describe()
df.cov()
df.corr()
df
df.reindex(['c','b','a','g'])
df.reindex(columns=['Varsova','Madrid','Paris'])
