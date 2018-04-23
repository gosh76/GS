# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 14:41:13 2018 by Goldie Sahni
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
plt.style.use('classic')
import numpy as np
x = np.linspace(0,10,100)
plt.plot(x,np.sin(x))
plt.show()
plt.plot(x,np.cos(x))
plt.plot(x,np.tan(x))
fig=plt.figure()
plt.plot(x,np.sin(x),'-')
fig.savefig('myfig2.png')
!dir *.png
%matplotlib inline
from IPython.display import Image
plt.subplot(2,1,1)
plt.plot(x,np.sin(x))
plt.subplot(2,1,2)
plt.plot(x,np.cos(x))
fig,ax=plt.subplots(2)
ax[0].plot(x,np.sin(x))
ax[1].plot(x,np.cos(x))
fig,ax=plt.subplots(3)
ax[0].plot(x,np.cos(x))
ax[1].plot(x,np.sin(x))
ax[2].plot(x,np.tan(x))
fig=plt.figure()
ax=plt.axes()
x = np.linspace(0,10,1000)
ax.plot(x,np.sin(x))
plt.plot(x,np.sin(x-0),color='blue')
plt.plot(x,np.sin(x-1),color='g')
plt.plot(x,x+0,linestyle='solid')
plt.plot(x,x+1,linestyle='dashdot')
plt.plot(x,np.sin(x))
plt.xlim(-1,11)
plt.ylim(1.2,-1.2)
plt.plot(x,np.sin(x),'-g',label='sin(x)')
plt.legend()
