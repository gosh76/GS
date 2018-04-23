# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 11:14:30 2018 by Goldie Sahni
"""
import numpy as np
a = np.arange(0,80,10)
a
y = a[[1,2,-3]]
y1 = a[[1,3,5,6]]
y1
y2 = [a[1],a[2],a[-3]]
y2
y3 = np.take(a,[1,2,-3])
#%%indexing
index1 = [1,2,-3]
y4=np.take(a,index1)
y4
mask = np.array([0,1,0,1,1,1,0,0],dtype=bool)
a[mask]
#%%calculation
np.sum(a)
a.sum
a.sum()
np.sum(a)
a.sum()
sum(a)
%timeit sum(a)
%timeit a.sum()
%timeit np.sum(a)
b = np.arange(0,80,5).reshape(4,4)
b
b.sum(axis=0)
b.sum(axis=1)
b.max(axis=0)
b.argmax(axis=0)
b.max(axis=None)
b.argmax(axis=None)
np.average(b,axis=0)
b.average()
b.mean()
np.average(b,weights=[1,2,3,4],axis=0)
a = np.array([[1,2,3],[4,5,6]],float)
a.clip(3,5)
a.ptp(axis=0)
a.flatten()
id(a)
a.ravel()
c=a.copy()
id(c)
b.resize(2,8)
b
a.resize(3,2)
d = np.array([1,2,3,4,5,6])
d.reshape(2,3)
d.reshape(6,1)
d.squeeze()
d
d.reshape(2,3)
d
e = d.reshape(2,3)
e
e.squeeze()
e
e.transpose()
e
e.nonzero()
e.sort(axis=-1)
e
f = e.copy()
e==f
