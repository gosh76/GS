# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 15:08:31 2018 by Goldie Sahni
"""

rollnoL = [109,102,105,106,103,110,101,107,104,111,108]
nameL = ['meena','apoorva','kaustav','shubham','goldie','hitesh','shruti','vijay',
         'achal','lalit','varun']
genderL=['F','F','M','M','M','M','F','M','M','M','M']
import numpy as np
import pandas as pd
pythonL=np.random.randint(60,90,11)
pythonL
sasL=np.random.randint(60,90,11)
sasL
nameS = pd.Series(nameL,index=rollnoL)
nameS
type(nameS)
n1 = pd.Series(nameL)
n1.index=rollnoL
n1
112 in n1.index
111 in n1.index
n1.index
n1.keys()
n1
n1.items
112 in n1
nameS.items
nameS.keys
nameS.values
list(nameS.items())
nameS.ix[108] = 'jain'
nameS
nameS[108]
nameS[108] = 'Jain'
nameS
nameS[:5]
nameS[0]
nameS[109]
nameS.iloc[0]
nameS.loc[109]
nameS[nameS=='meena']
nameS.loc[103:110]
df1 = pd.DataFrame(rollnoL)
df2 =pd.DataFrame(nameL)
df2['rollnoL'] = rollnoL
rollnoS = pd.Series(rollnoL)
nameS = pd.Series(nameL)

genderS = pd.Series(genderL)
pythonS=pd.Series(pythonL)
sasS = pd.Series(sasL)
df3 = pd.concat([rollnoS,nameS,genderS,pythonS,sasS],axis=1)
df3
df3.columns = ['roll','name','gender','py','sas']
df4 = pd.DataFrame({'roll':rollnoL,'name':nameL,'gender':genderL,'python':pythonL,'sas':sasL})
df4
df4.columns = ['roll','name','gender','python','sas']
df4
del df4
df5 = pd.DataFrame({'roll':rollnoL,'name':nameL,'gender':genderL,'python':pythonL,'sas':sasL},columns=['roll','name','gender','python','sas'])
df5
df6 = df5[['roll','name']]
df6
df6.dtypes
df6.values
df6.values[0]
df6.values[0][1]
df6.t
df6.T
df6.loc[0,:]
df6.iloc[0]
df6
df5.iloc[0]
df5[:4,:3]
df5.iloc[:4,:3]
df5
df5['total'] = df5['python'] + df5['sas']
df5
df5.loc[df5.total>150,:]
df5.iloc[0:5]
for x in range(1,11):
    for y in range(1,11):
        2*x + 3*y = 35
    print(x,y)

df5
courseL = ['pg','pg','msc','msc','pg','pg','pg','pg','pg','pg','bsc']
hadoopL = np.random.randint(71,90,11)
feesL = np.random.randint(100000,150000,11)
hostelL = [True,True,True,False,True,True,True,False,False,True,True]
df5['course'] = courseL
df5['hadoop'] = hadoopL
df5['fees'] = feesL
df5['hostel'] = hostelL
df5
df5.to_csv('df5.csv')
df5.columns
df5.groupby('gender').mean()
from numpy import random
classes = ['C1','C2','C3']
sclass = random.choice(classes,11)
df5['sclass']=sclass
df5
df5.to_csv('df5.csv')
pd.pivot_table(df5,index=['name'])
df5
pd.pivot_table(df5,index=['name','sclass','hostel'])
pd.pivot_table(df5,index=['course','sclass'],values=['total','python'])
pd.pivot_table(df5,index=['course','sclass'],values=['total','python'],aggfunc=np.sum)
