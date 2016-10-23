# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 21:08:38 2016

@author: admin12
"""

import pylab as pl
import math
import numpy
B_m=4*10**-5
T=273
a=6.5*10**-3
alpha=2.5
class cannon:
    def __init__(self, x, y, v,time_step):
        self.x=[x]
        self.y=[y]
        self.v=v
        self.vx=v*math.cos(math.pi/4)
        self.vy=v*math.sin(math.pi/4)
        self.dt=time_step
        self.fm=[]
    def run(self):
        while(self.y[-1] >= 0):
            Newv = math.sqrt(self.vx**2 + self.vy**2)
            self.vx = self.vx - ((1 - a*self.y[-1]/T)**alpha)*B_m*Newv*self.vx*self.dt
            self.vy = self.vy - 9.8*self.dt - ((1 - a*self.y[-1]/T)**alpha)*B_m*Newv*self.vy*self.dt
            self.x.append(self.x[-1] + self.vx*self.dt)
            self.y.append(self.y[-1] + self.vy*self.dt)
        r1 = -self.y[-2]/self.y[-1]
        self.x[-1] = (self.x[-2] + r1*self.x[-1])/(r1 + 1)
        self.y[-1] = 0
        self.fm.append(max(self.y))
    def show_results(self):
        font = {'family': 'serif',
                'color':  'black',
                'weight': 'normal',
                'size': 15,
                }
        plot, = pl.plot(self.x, self.y, 'r')
        pl.title('Cannon shell trajectory', fontdict = font)
        pl.xlabel('x asix(m)')
        pl.ylabel('y asix(m)')
        print"target altitude: %dm, munium velocity:%dm/s"%(self.fm[0],self.v)
for j in numpy.linspace(100, 700,10):
    c=cannon(0,0,j,0.01)
    c.run()
    c.show_results()

