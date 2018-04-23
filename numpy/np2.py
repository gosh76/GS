# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 11:20:58 2018 by Goldie Sahni
"""

import numpy as np
a = np.array([1,2,3,4,5])
a
a.fill(5)
a
a[1]=45
a
a.type
type(a)
np.shape(a)
a.shape
a = np.array([[0,1,2,3],[10,11,12,13]])
a.shape
a.size
a.ndim
a
np.shape(a)
a[1,3]
a[2,3]
a[0,1:]
a[:,0::2]
a = np.array([[1,2,3],[4,5,6]],float)
a
print(a.shape)
print(a.dtype.type)
type(a[0,0]) is type(a[1,2])
b = a[:,::2]
b
b[0,1] = 100
a
c = a[:,::2].copy()
c
a = np.arange(0,80,10)
a
y = a[[1,2,-3]]
y
y = np.take(a,[1,2,-3])
y
mask = np.array([0,1,1,0,0,1,0,0],dtype=bool)
y=a[mask]
y
mask1 = np.array([True,False,False,False,False,False,False,True],dtype=bool)
a[mask1]
np.arange(0,56).reshape(2,-2)
a = np.arange(0,36).reshape(6,6)
a[(0,1,2,3,4),(1,2,3,4,5)]
a[3:,[0,2,5]]
mask = np.array([1,0,1,0,0,1],dtype=bool)
a[mask,2]
sum(a)
a = np.array([[1,2,3],[4,5,6]],float)
sum(a)
a.sum()
a.prod(axis=1)
a.argmin()
a.mean()
a.mean(axis=1)
a.clip(3,5)
a.round()
a.ptp(axis=0)
a.ptp(axis=None)
