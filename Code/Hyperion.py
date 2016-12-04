# -*- coding: utf-8 -*-
"""
Created on Sat Dec 03 14:56:47 2016

@author: admin12
"""

import math
import matplotlib.pyplot as plt

GMs = 4 * (math.pi**2)

def initial(a,e): 
    x0=a*(1+e) 
    y0=0 
    v_x0=0 
    v_y0=2 * math.pi * math.sqrt((1-e)/(a*(1+e))) 
    return [x0,y0,v_x0,v_y0]

def orbit(a, e, theta0, dt, total_time):
    q = initial(1 ,e)
    x0 = q[0]
    y0 = q[1]
    v_x0 = q[2]
    v_y0 = q[3]
    x = [x0]
    y = [y0]
    vx = [v_x0]
    vy = [v_y0]
    t = [0]
    omega = [0]
    theta = [theta0]
    while t[-1] < total_time:
        r=math.sqrt(x[-1]**2 + y[-1]**2)
        newvx = vx[-1] - GMs * x[-1] / (r ** 3) * dt
        newx = x[-1] + newvx * dt
        newvy = vy[-1] - GMs * y[-1] / (r ** 3) * dt
        newy = y[-1] + newvy * dt
        vx.append(newvx)
        vy.append(newvy)
        x.append(newx)
        y.append(newy)
        newomega = omega[-1] - 3 * GMs / (r ** 5) * (x[-1] * math.sin(theta[-1]) - y[-1] * math.cos(theta[-1])) * (x[-1] * math.cos(theta[-1]) + y[-1] * math.sin(theta[-1])) * dt
        newtheta = theta[-1] + newomega * dt
        if newtheta >= math.pi:
            newtheta = newtheta - 2 * math.pi
        if newtheta <= -math.pi:
            newtheta = newtheta + 2 * math.pi
        omega.append(newomega)
        theta.append(newtheta)
        t.append(t[-1] + dt)
    return [vx, vy, x, y, omega, theta, t]

def dtheta(theta1, theta2):
    delta_theta = []
    for i in range(len(theta1)):
        delta_theta.append(abs(theta1[i] - theta2[i]))
    return delta_theta

A = orbit(1, 0.7, 0, 0.0001, 7)
A_theta = A[5]
A_omega = A[4]
A_t = A[6]
x1 = A[2]
y1 = A[3]

B = orbit(1, 0.7, 0.01, 0.0001, 7)
B_theta = B[5]
B_omega = B[4]
B_t = B[6]

C = orbit(1, 0.3, 0, 0.0001, 7)
C_theta = C[5]
C_omega = C[4]
C_t = C[6]

D = orbit(1, 0.3, 0.01, 0.0001, 7)
D_theta = D[5]
D_omega = D[4]
D_t = D[6]

angle = dtheta(A_theta, B_theta)
angle1 = dtheta(C_theta, D_theta)

plt.figure(figsize=[10,5])
plt.subplot(121)
plt.plot(C_t, angle)
plt.title('$\Delta\\theta$ versus time')
plt.xlabel('time(yr)')
plt.ylabel('$\Delta\\theta$(radians)')
plt.text(3,0.00001,'Elliptical obit($e=0.7$)')
plt.semilogy(0.0001, 0.1)
plt.subplot(122)
plt.plot(C_t, angle1)
plt.title('$\Delta\\theta$ versus time')
plt.xlabel('time(yr)')
plt.ylabel('$\Delta\\theta$(radians)')
plt.text(3,0.0000004,'Ellipticalr obit($e=0.3$)')
plt.semilogy(0.0001, 0.1)
plt.savefig('r',dpi=144)
    
        
    