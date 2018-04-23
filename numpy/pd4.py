# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 11:13:23 2018 by Goldie Sahni
"""

import numpy as np
import pandas as pd
rng = np.random.RandomState(42)
marks = pd.Series(rng.randint(50,100,11))
marks
marks.sum()
marks.std()
marks1 = pd.Series(rng.randint(50,100,11))
marks==marks1
marks1.sum()
dict(x=1,y=4)
rng = np.random.RandomState(56)
df = pd.DataFrame({'A':rng.randint(5,8,6),'B':rng.randint(5,8,6)})
df
df.sum()
df.mean()
df.mean(axis=0)
df.mean(axis=1)
df.mean(axis='columns')
df.mean(axis='rows')
df.sum(axis=0)
df.sum(axis=1)
df1 = pd.DataFrame({'Name':['A','B','C','C','A','B','C','A'],'Value':rng.randint(1,100,8)})
df1
df1.groupby('Name').sum()
df1.groupby('Name').mean()
np.repeat(['A','B','C'],2)
np.repeat(['A','B','C'],[1,2,3])
df2 = pd.DataFrame({'key':['A','B','C']*2,'data1':range(6),'data2':rng.randint(0,10,6)})
df2
df2.groupby('key').aggregate(['min','max','median'])
df2.groupby('key').aggregate([np.median,np.sum])
df2.groupby('key').aggregate({'data1':'min','data2':['max','min']})
df2.filter(items=['key','data1'])
df2.filter(like='2',axis=0)
grouped = df2.groupby('key')
grouped.filter(lambda x:x['data2'].mean()>4)
grouped.filter(lambda x:x['data2'].std()>4)
x=2
y=3
p1 = lambda x,y:x*y
p1
p1(x,y)
grouped.transform(lambda x:x-x.mean())
grouped.apply(lambda x:x['data2']*2)
df2.groupby('key').sum()
df3 = df2.set_index('key')
df3
newmap = {'A':'PG','B':'MS','C':'BS'}
df3.groupby(newmap).sum()
df3.groupby(str.lower).mean()
df3.groupby([str,str.lower,newmap]).mean()
studentdf = pd.read_csv('~/GSpython/df5.csv')
studentdf
pwd()
studentdf.drop(['Unnamed: 0'],axis=1,inplace=True)
studentdf
studentdf.describe()
studentdf.index=studentdf.roll
studentdf
studentdf.groupby('course')['sclass'].describe()
studentdf[['sclass','python','sas']].groupby('sclass').aggregate(['min',np.sum])
