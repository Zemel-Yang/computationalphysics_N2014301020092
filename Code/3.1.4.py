# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 19:27:31 2016

@author: admin12
"""
import matplotlib.pyplot as plt
import numpy as np
        
class billiard_innercircle:
    def __init__(self,x_0,y_0,vx_0,vy_0,N,dt):
        self.x_0 = x_0
        self.y_0 = y_0
        self.vx_0 = vx_0
        self.vy_0 = vy_0
        self.N = N
        self.dt = dt
    def motion_calculate(self):
        self.x = []
        self.y = []
        self.vx = []
        self.vy = []
        self.t = [0]
        self.x.append(self.x_0)
        self.y.append(self.y_0)
        self.vx.append(self.vx_0)
        self.vy.append(self.vy_0)
        for i in range(1,self.N):
            self.x.append(self.x[i - 1] + self.vx[i - 1]*self.dt)
            self.y.append(self.y[i - 1] + self.vy[i - 1]*self.dt)
            self.vx.append(self.vx[i - 1])
            self.vy.append(self.vy[i - 1])
            if (self.x[i] < -1.0):
                self.x[i],self.y[i] = self.correct('x>-1.0',self.x[i - 1], self.y[i - 1], self.vx[i - 1], self.vy[i - 1])
                self.vx[i] = - self.vx[i]
            elif(self.x[i] > 1.0):
                self.x[i],self.y[i] = self.correct('x<1.0',self.x[i - 1], self.y[i - 1], self.vx[i - 1], self.vy[i - 1])
                self.vx[i] = - self.vx[i]
            elif(self.y[i] < -1.0):
                self.x[i],self.y[i] = self.correct('y>-1.0',self.x[i - 1], self.y[i - 1], self.vx[i - 1], self.vy[i - 1])
                self.vy[i] = -self.vy[i]
            elif(self.y[i] > 1.0):
                self.x[i],self.y[i] = self.correct('y<1.0',self.x[i - 1], self.y[i - 1], self.vx[i - 1], self.vy[i - 1])
                self.vy[i] = -self.vy[i] 
            elif((self.x[i] - 0.05)**2+self.y[i]**2<0.01):
                self.x[i],self.y[i] = self.correct('(x - 0.05)**2+y**2 > 0.01',self.x[i - 1], self.y[i - 1], self.vx[i - 1], self.vy[i - 1])
                self.vx[i],self.vy[i] = self.reflect(self.x[i]-0.05,self.y[i],self.vx[i - 1], self.vy[i - 1])
            self.t.append(self.t[i - 1] + self.dt)
        return self.x, self.y    
               
        
    def plot_boundary(self):
        theta = 0
        x = []
        y = []
        plt.title('Slightly off-center')
        while theta < 2*np.pi:
            x.append(0.1*np.cos(theta)+0.05)
            y.append(0.1*np.sin(theta))
            theta+= 0.01
        plt.plot(x,y,'black')
    def plot(self):
        plt.figure(figsize = (8,6))
        plt.xlim(-1,1)
        plt.ylim(-1,1)
        plt.xlabel('x')
        plt.ylabel('y')
        self.plot_boundary()
        plt.plot(self.x,self.y,'green')
        plt.savefig('chapter3_3.31_4.png',dpi = 144)
        plt.show()
    def correct(self,condition,x,y,vx,vy):
        vx_c = vx/100.0
        vy_c = vy/100.0
        while eval(condition):
            x = x + vx_c*self.dt
            y = y + vy_c*self.dt
        return x-vx_c*self.dt,y-vy_c*self.dt
    def reflect(self,x,y,vx,vy):
        module = np.sqrt(x**2+y**2)  ### normalization
        x = x/module
        y = y/module
        v = np.sqrt(vx**2+vy**2)
        cos1 = (vx*x+vy*y)/v
        cos2 = (vx*y-vy*x)/v
        vt = -v*cos1
        vc = v*cos2 
        vx_n = vt*x+vc*y
        vy_n = vt*y-vc*x
        return vx_n,vy_n
A = billiard_innercircle(0.5,0.5,0.47,0.323,4000,0.1)
A.motion_calculate()
A.plot()