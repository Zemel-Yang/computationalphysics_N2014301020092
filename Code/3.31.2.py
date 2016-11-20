# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 18:54:06 2016

@author: admin12
"""

import matplotlib.pyplot as plt
import numpy as np
class billiard_circle:
    def __init__(self,x_0,y_0,vx_0,vy_0,N,dt):
        self.x_0 = x_0
        self.y_0 = y_0
        self.vx_0 = vx_0
        self.vy_0 = vy_0
        self.N = N
        self.dt = dt
    
    def correct(self,condition,x,y,vx,vy):
        vx_c = vx/100.0
        vy_c = vy/100.0
        while eval(condition):
            x = x + vx_c*self.dt
            y = y + vy_c*self.dt
        return x-vx_c*self.dt,y-vy_c*self.dt
        
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
            if (np.sqrt( self.x[i]**2+self.y[i]**2 ) > 1.0):
                self.x[i],self.y[i] = self.correct('np.sqrt(x**2+y**2) < 1.0',self.x[i - 1], self.y[i - 1], self.vx[i - 1], self.vy[i - 1])
                self.vx[i],self.vy[i] = self.reflect(self.x[i],self.y[i],self.vx[i - 1], self.vy[i - 1])
            self.t.append(self.t[i - 1] + self.dt)
        return self.x, self.y
        
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
        
    def plot(self):
        plt.figure(figsize = (8,8))
        plt.xlim(-1,1)
        plt.ylim(-1,1)
        plt.xlabel('x')
        plt.ylabel('y')
        self.plot_boundary()
        plt.plot(self.x,self.y)
        plt.title('Circular stadium - trajectory')
        plt.savefig('chapter3_3.31.7.png',dpi = 144)
        plt.show()
        
    def phase_space_plot(self):
        plt.figure(figsize = (16,8))
        plt.subplot(121)
        plt.xlabel('x')
        plt.ylabel(r'$v_x$')
        plt.scatter(self.x,self.vx, s=1)
        plt.subplot(122)
        plt.xlabel('y')
        plt.ylabel(r'$v_x$')
        plt.scatter(self.y,self.vx, s=2)
        plt.title('$v_x$-x')
        plt.savefig('chapter3_3.31_phase.png', dpi= 144)
        plt.show()
    
    def phase_plot(self):
        plt.figure(figsize = (8,8))
        record_x = []
        record_vx = []
        for i in range(len(self.x)):
            if (abs(self.y[i] - 0)<0.001):
                record_vx.append(self.vx[i])
                record_x.append(self.x[i])
        plt.xlabel('x')
        plt.ylabel(r'$v_x$')
        plt.scatter(record_x,record_vx,s=1)
        plt.savefig('chapter3_3.31_phasey=0.png', dpi= 144)
        plt.show()
                
        
    def plot_boundary(self):
        theta = 0
        x = []
        y = []
        while theta < 2*np.pi:
            x.append(np.cos(theta))
            y.append(np.sin(theta))
            theta+= 0.01
        plt.plot(x,y,'black')
A = billiard_circle(0.5,0.5,0.47,0.323,4000,0.1)
A.motion_calculate()
A.plot()
A.phase_plot()
A.phase_space_plot()
