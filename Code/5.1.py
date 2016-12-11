# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 19:29:48 2016

@author: admin12
"""

import numpy as np
from pylab import *
from math import *
import mpl_toolkits.mplot3d
# initialize : i represents x, j represents y
V0=[[0 for i in range(21)]for j in range(21)]
for i in range(6,15):
    for j in range(6,15):
        V0[j][i]=1.0# j,i
#check
for j in range(len(V0)):
    for i in range(len(V0[1])):
        print V0[i][j], 
    print
"""
#capacitor initialization
for i in [6]:
    for j in range(6,15):
        V0[j][i]=1.0
for i in [-6]:
    for j in range(6,15):
        V0[j][i]=1.0       
"""
VV=[]
VV.append(V0)
s=0
dx=0.1
#calculate:update V and delta_V
while 1:
    VV.append(V0)
    for i in range(1,len(V0)-1):
        for j in range(1,len(V0[1])-1):
            VV[s+1][i][j]=(VV[s][i+1][j]+VV[s][i-1][j]+\
                          VV[s][i][j+1]+VV[s][i][j-1])/4.0
    for i in range(6,15):
        for j in range(6,15):
            VV[s+1][j][i]=1.0
    for i in [20]:
        for j in range(21):
            VV[s+1][j][i]=0.0
    for i in [-20]:
        for j in range(21):
            VV[s+1][j][i]=0.0
    for j in [20]:
        for i in range(21):
            VV[s+1][j][i]=0.0
    for j in [-20]:
        for i in range(21):
            VV[s+1][j][i]=0.0
"""
    #capacitor calculation
    for i in [6]:
        for j in range(6,15):
            V0[j][i]=1.0
        for i in [-6]:
            for j in range(6,15):
                V0[j][i]=1.0       
"""
#calculate delta_V
    VV[s]=np.array(VV[s])
    VV[s+1]=np.array(VV[s+1])
    dVV=VV[s+1]-VV[s]
    dV=0
    for i in range(1,len(V0)-1):
        for j in range(1,len(V0[1])-1):
            dV=dV+abs(dVV[i][j])
    #print dV 

    s=s+1
    if dV<0.0001 and s>10:
        break
print s
#display final results
#Equipotential lines
figure(figsize=[8,8])
x=np.arange(-1.0,1.01,dx)#-1.0,-0.9,...,1.0
y=np.arange(-1.0,1.01,dx)
X,Y=np.meshgrid(x,y)
CS = contour(X,Y,V,15)
clabel(CS, inline=1, fontsize=10)
xlim(-1,1)
xlabel('x')
ylim(-1,1)
ylabel('y')
title('Equipotential lines of electric potential', fontsize=15)
#3D plot
fig = figure(figsize=[8,8])
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, V,rstride=1, cstride=1,linewidth=0)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('V')
title('Electric potential', fontsize=15)

#Electic field

V=array(VV[-1])
Ex=array(V0)
Ey=array(V0)
for j in range(1,len(V0)-1):
    for i in range(1,len(V0[1])-1):
        Ex[j][i]=-(V[j][i+1]-V[j][i-1])/(2*dx)
        Ey[j][i]=-(V[j+1][i]-V[j-1][i])/(2*dx)

figure(figsize=[8,8])
Q=quiver(X,Y,Ex,Ey,scale=100)
xlim(-1,1)
xlabel('x')
ylim(-1,1)
ylabel('y')
title('Electric field', fontsize=15)
show()

    delta_V = 0

    for i in range(101):    
        for j in range(101):
            if i == 0 or i == 100 or j == 0 or j == 100:
                pass
            elif 40<=i<=70 and j == 40:
                pass
            elif 40<=i<=70 and j == 70:
                pass
            else:
                voltage_new = (v[i+1][j]+v[i-1][j]+v[i][j+1]+v[i][j-1])/4
                voltage_old = v[i][j]
                delta_V += abs(voltage_new - voltage_old)
                v[i][j] = voltage_new

    return v, delta_V
    
def Laplace_calculate(v):
    
    epsilon = 10**(-5)*100**2
    delta_V = 0
    N_iter = 0

    while delta_V >= epsilon or N_iter <= 10:
        v1, delta_V = update_V(v)
        v2, delta_V = update_V(v1)
        v = v2
        N_iter += 1

    return v2


x = np.linspace(0,100,101)
y = np.linspace(0,100,101)
X, Y = np.meshgrid(x, y)
Z = Laplace_calculate(v)
Ex = deepcopy(Z)
Ey = deepcopy(Z)
E = deepcopy(Z)

for i in range(101):
    for j in range(101):
        if i == 0 or i == 100 or j == 0 or j == 100:
            Ex[i][j] = 0
            Ey[i][j] = 0
        else:
            Ex_value = -(Z[i+1][j] - Z[i][j])/2
            Ey_value = -(Z[i][j+1] - Z[i][j])/2
            Ex[i][j] = Ex_value
            Ey[i][j] = Ey_value

for i in range(101):
    for j in range(101):
        E_value = np.sqrt(Ex[i][j]**2 + Ey[i][j]**2)
        E[i][j] = E_value
   
plt.figure()
CS = plt.contour(X,Y,Z, 8, alpha=.75, cmap='jet')
plt.clabel(CS, inline=1, fontsize=12)
plt.colorbar(CS)
plt.title('voltage near capacitor')
plt.xlabel('x(m)')
plt.ylabel('y(m)')

fig = figure()
ax = Axes3D(fig)
surf=ax.plot_surface(X, Y, Z,rstride=1, cstride=1, cmap=cm.coolwarm,linewidth=0, antialiased=False) 
ax.xlabel('x(m)') 
ax.set_ylabel('y(m)') 
ax.set_zlabel('voltage(V)') 
ax.set_title('voltage distribution') 
fig.colorbar(surf,shrink=0.5,aspect=5)
         
fig0, ax0 = plt.subplots()
strm = ax0.streamplot(X, Y, np.array(Ey), np.array(Ex), color=np.array(E), linewidth=2, cmap=plt.cm.autumn)
fig0.colorbar(strm.lines)
ax0.set_xlabel('x(m)')
ax0.set_ylabel('y(m)')
ax0.set_title('Electric field')
plt.show()