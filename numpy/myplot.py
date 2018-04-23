# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 15:03:10 2018 by Goldie Sahni
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
plt.style.use('classic')
import numpy as np
x = np.linspace(0,10,100)
plt.plot(x,np.sin(x))
plt.show()

