# -*- coding: utf-8 -*-
"""
Created on Fri Jan 06 22:20:39 2017

@author: admin12
"""

import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy
import matplotlib.cm as cm
from mpl_toolkits.mplot3d import Axes3D

def density(t_end):

    x = np.linspace(-50,50,101)
    y = np.linspace(-50,50,101)
    x,y = np.meshgrid(x,y)
    d = np.zeros((101,101))
    d[50][50]=1
    d1 = deepcopy(d)

    for t in range(t_end):
        for i in range(101):
            for j in range(101):
                if i==0 or i==100 or j==0 or j==100:
                    pass
                else:
                    d[i][j]=0.25*(d1[i+1][j] + d1[i-1][j] + d1[i][j+1] + d1[i][j-1])
        d1=deepcopy(d)

    for i in range(101):
            for j in range(101):
                if i==0 or i==100 or j==0 or j==100:
                    pass
                else:
                    if d[i][j]==0:
                        d[i][j]=0.25*(d1[i+1][j] + d1[i-1][j] + d1[i][j+1] + d1[i][j-1])

    return x,y,d



fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')
x,y,z = density(100)[0],density(100)[1],density(100)[2]
ax1.plot_surface(x, y, z,rstride=2, cstride=2, cmap='rainbow')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_zlabel('density')
ax1.set_title('Distribution in 2 dimension, t=100')
plt.savefig('6.png',dpi=144)

plt.show()