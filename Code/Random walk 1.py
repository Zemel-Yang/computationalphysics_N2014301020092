# -*- coding: utf-8 -*-
"""
Created on Fri Jan 06 11:28:14 2017

@author: admin12
"""

import random
import matplotlib.pyplot as pl
x = 0
y = 0
a = [0]
b = [0]
c = [[] for q in range(500)]
d = []
s =[0]
w = []
i = 0
j = 0
k = 0
l = [0, 10 ,20 ,30 ,40 ,50 ,60, 70, 80, 90, 100]
m = [0,0,0,0,0,0,0,0,0,0,0]
n = [0,100]
o = [0,100]
z = 0
ctotal = 0
while i < 100:
    r = random.random()
    if r < 0.5:
        x = x + 1
    else:
        x = x -1
    a.append(x)
    s.append(i + 1)
    i += 1
while j < 100:
    r = random.random()
    if r < 0.5:
        y = y + 1
    else:
        y = y -1
    b.append(y)
    j += 1
while k < 500:
    v = 0
    z = 0
    while v < 100:
        r = random.random()
        if r < 0.5:
            z = z + 1
        else:
            z = z - 1
        c[k].append(z)
        v += 1
    k += 1
for t in range(100):
    ctotal = 0
    for u in range(500):
        ctotal = ctotal + c[u][t]**2
    d.append(ctotal/500)
    w.append(t)
    
    

        
    
pl.figure(figsize=[13,5])
pl.subplot(121)
pl.scatter(s,a)
pl.scatter(s,b,color='m')
pl.plot(l,m,'--')
pl.title('Random walk in one dimension')
pl.xlabel('step number')
pl.ylabel('x')
pl.xlim(0,100)
pl.subplot(122)
pl.plot(w,d,'b.')
pl.plot(n,o,'red')
pl.xlabel('step numbeer(= time)')
pl.ylabel('<$x^2$>')
pl.title('Random walk in one dimension')
pl.text(20,81,'<$x^2$>versus time')
pl.savefig('figure 7.2.png',dpi=144)
pl.show()