# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 12:28:20 2018 by Goldie Sahni
"""


import numpy as np
import pandas as pd
import csv
df5 = pd.read_csv('~/GSpython/df5.csv')
pd.pivot_table(df5,index='course',values=['sas','hadoop'],aggfunc=[np.mean,np.median,min,max])
%matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


pd.pivot_table(df5,index='gender',columns='sclass',values='sas').plot(kind='bar')
aggregation = {'sas':{'totalsas':'sum','avgsas':'mean'},'hadoop':{'meanh':'mean','stdh':'std'}}
df5[df5.sclass=='C1'].groupby('gender').agg(aggregation)
df5.groupby(['gender','sclass']).agg({'python':{'t1':np.mean,'t2':np.median}})

x = [1,2,3]
y = [2,4,1]
plt.plot(x,y)
plt.show()
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
x1 = [1,2,3]
y1 = [4,1,3]
plt.plot(x,y,label='line1')
plt.plot(x1,y1,label='line2')
plt.xlabel('X')
plt.ylabel('Y')
plt.bar(x1,y1,15)
marks = np.random.uniform(30,100,1000)
bins=10
range=(20,100)
plt.hist(marks,bins,range,color='green',histtype='bar',rwidth=0.8)
plt.pie(y,startangle=45,explode=(0.5,0,0))
