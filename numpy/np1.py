# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 11:27:31 2018 by Goldie Sahni
"""

import numpy
numpy.__version__
import numpy as np
import array
L=list(range(10))
A=array.array('i',L)
A
np.array([1,4,2,5,3])
np.array([1,2,3,4],dtype='float32')
np.zeros(10,dtype=int)
np.ones((3,5),dtype=float)
np.full((3,5),3.14)
np.full((3,5),5)
n1 = np.arange(0,20,2)
len(n1)
np.linspace(0,1,5)
np.random.random((3,3))
np.random.normal(0,1,(3,3))
np.random.randint(0,1)
np.empty(3)
np.random.seed(0)
x1 = np.random.randint(10,size=(3,4,5))
x1
x1.ndim
x1.shape
x1.size
x1.itemsize
x1.nbytes
x1[0,0,0]
x1[0,:,:]
x = np.arange(10)
x
x[:5]
x[5:]
x[::2]
x[1::2]
x[::-1]
x[5::-2]
x1[0,::-1,::-1]
