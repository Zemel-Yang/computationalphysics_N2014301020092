# -*- coding: utf-8 -*-
"""
Created on Fri Jan 06 23:44:16 2017

@author: admin12
"""

import random
import numpy as np
import matplotlib.pyplot as plt
import math
def randpath(tt):
    y=[]
    x=[]
    x.append(tt)
    y.append(tt)
    for i in range(tt):
        cc=random.random()
        if cc<=0.25:
           x.append(x[-1])
           y.append(y[-1]+1)
        elif cc<=0.5:
           x.append(x[-1])
           y.append(y[-1]-1)
        elif cc<=0.75:
           x.append(x[-1]-1)
           y.append(y[-1])
        else:
           x.append(x[-1]+1)
           y.append(y[-1])
                         
    return x,y
ss=[]
ty=640
c1=[0]*(2*ty+1)
bn=5000
t=[]
for g in range(1,ty,5):
    t.append(g)
    s=0
    ct=[]
    for i in range(2*ty+1):
        ct.append(c1[:])
    for i in range(1,bn):
        a,b=randpath(g)
        ct[a[-1]][b[-1]]=ct[a[-1]][b[-1]]+1.0/bn
    for j in range(len(ct)):
        for k in range(len(ct)):
            if ct[j][k]!=0:
               s=s-ct[j][k]*math.log(ct[j][k])
    ss.append(s)              
plt.plot(t,ss,'r')
plt.xlim(0,640)
plt.xlabel('time')
plt.ylabel('Entropy')
plt.title('Enropy versus time')
plt.text(250,4,'Mixing of scream in coffee')
plt.savefig('90.png',dpi=144)
plt.show()
             