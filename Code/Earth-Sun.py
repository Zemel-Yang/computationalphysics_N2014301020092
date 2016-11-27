# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 22:53:13 2016

@author: admin12
"""

import math
import matplotlib.pyplot as plt

GMs = 4 * (math.pi**2)

class earth_sun():
    def __init__(self, vx, vy, time_step, total_time):
        self.x = [1]
        self.y = [0]
        self.vx = [vx]
        self.vy = [vy]
        self.dt = time_step
        self.t = [0]
        self.total_time = total_time
    def calculate(self):
        while self.t[-1] < self.total_time:
             r=math.sqrt(self.x[-1]**2+self.y[-1]**2)
             newvx = self.vx[-1] - (GMs * self.x[-1] / r**3) * self.dt
             newx = self.x[-1] + newvx * self.dt
             newvy = self.vy[-1] - (GMs * self.y[-1] / r**3) * self.dt
             newy=self.y[-1] + newvy * self.dt
             self.vx.append(newvx)
             self.vy.append(newvy)
             self.x.append(newx)
             self.y.append(newy)
             self.t.append(self.t[-1] + self.dt)
    def plot(self,color='k', slogan=''):
        plt.plot(self.x,self.y,color,label=slogan)
        plt.ylim(-2,2)
        plt.xlabel('x(AU)')
        plt.ylabel('y(AU)')
        plt.title('Earth orbiting the Sun')
        plt.savefig('1.png',dpi=144)
        plt.show()

A = earth_sun(0, 2*math.pi, 0.01, 1)
A.calculate()
A.plot(color='r',slogan='$v_y=2\pi$')

    

