# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 11:11:55 2016

@author: admin12
"""

import matplotlib.pyplot as pl
import math
class chaos:
    def __init__(self, theta,w,F,time_step):
        self.theta = [theta]
        self.w = [w]
        self.g = 9.8
        self.dt = 0.04
        self.t = [0]
        self.pendulum_length = 9.8
        self.q = 0.5
        self.F = F
        self.OMIGA_D = 2.0 / 3
        self.g_l = self.g / self.pendulum_length
        self.dt = time_step
        self.t1=[0]

    def run(self):
        for i in range(1,1000000):
            self.theta.append(self.theta[i - 1] + self.w[i - 1] * self.dt)
            self.t.append(self.t[i - 1] + self.dt)
            self.w.append(self.w[i - 1] - (self.g_l * math.sin(self.theta[i]) + self.q * self.w[i - 1] - self.F * math.sin(self.OMIGA_D *self.t[i])) * self.dt)
            if self.theta[-1] >= math.pi:
                self.theta[-1] = -2 * math.pi + self.theta[-1]

            elif self.theta[-1] <= -math.pi:
                self.theta[-1] = self.theta[-1] + 2 * math.pi
    def show_results(self):
        for i in range(len (self.t)):
            x=(self.OMIGA_D * self.t[i]) / (2*math.pi)
            #x=(self.OMIGA_D * self.t[i]) / (2*math.pi) - 1.0 / 8.0
            #x=(self.OMIGA_D * self.t[i]) / (2*math.pi) - 1.0 / 4.0
            if  abs(x - round(x)) <= 0.001:
                self.t1.append(self.t[i])
                pl.scatter([self.theta[i], ], [self.w[i], ], 1, color ='red')
        #pl.title('$w$ versus $\ theta$ Fd=0.5')
        pl.title('$w$ versus $\ theta$ Fd=0.5')
        pl.xlabel('$\ theta$(radians)')
        pl.ylabel('$w$(radians/s)')
        pl.savefig('chapter3_3.12.png',dpi=144)
        pl.show()
#a=chaos(0.2,0,0.5,0.04)
#a.run()
#a.show_results()

a=chaos(0.2,0,0.5,0.04)
a.run()
a.show_results()
