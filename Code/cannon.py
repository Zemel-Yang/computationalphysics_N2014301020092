#-*-coding:utf-8-*-
"""
Created on Sun Oct 16 15:56:50 2016

@author: admin12
"""

import pylab as pl
import math
class cannon:
    def __init__(self, x=0, y=0, v=700, time_step=0.1, B_m=4*10**-5, T=273, a=6.5*10**-3, alpha=2.5):
        self.vx1 = v*math.cos(math.pi/4)
        self.vy1 = v*math.sin(math.pi/4)
        self.vx2 = v*math.cos(math.pi/3)
        self.vy2 = v*math.sin(math.pi/3)
        self.vx3 = v*math.cos(math.pi/6)
        self.vy3 = v*math.sin(math.pi/6)
        self.vx4 = v*math.cos(math.pi/180*50)
        self.vy4 = v*math.sin(math.pi/180*50)
        self.vx5 = v*math.cos(math.pi/180*40)
        self.vy5 = v*math.sin(math.pi/180*40)
        self.x1 = [x]
        self.y1 = [y]
        self.x2 = [x]
        self.y2 = [y]
        self.x3 = [x]
        self.y3 = [y]
        self.x4 = [x]
        self.y4 = [y]
        self.x5 = [x]
        self.y5 = [y]
        self.dt = time_step
        self.B_m = B_m
        self.T = T
        self.a = a
        self.alpha = alpha
    def run(self):
        while(self.y1[-1] >= 0):
            Newv1 = math.sqrt(self.vx1**2 + self.vy1**2)
            self.vx1 = self.vx1 - ((1 - self.a*self.y1[-1]/self.T)**self.alpha)*self.B_m*Newv1*self.vx1*self.dt
            self.vy1 = self.vy1 - 9.8*self.dt - ((1 - self.a*self.y1[-1]/self.T)**self.alpha)*self.B_m*Newv1*self.vy1*self.dt
            self.x1.append(self.x1[-1] + self.vx1*self.dt)
            self.y1.append(self.y1[-1] + self.vy1*self.dt)
        r1 = -self.y1[-2]/self.y1[-1]
        self.x1[-1] = (self.x1[-2] + r1*self.x1[-1])/(r1 + 1)
        self.y1[-1] = 0
        while(self.y2[-1] >= 0):
            Newv2 = math.sqrt(self.vx2**2 + self.vy2**2)
            self.vx2 = self.vx2 - ((1 - self.a*self.y2[-1]/self.T)**self.alpha)*self.B_m*Newv2*self.vx2*self.dt
            self.vy2 = self.vy2 - 9.8*self.dt - ((1 - self.a*self.y2[-1]/self.T)**self.alpha)*self.B_m*Newv2*self.vy2*self.dt
            self.x2.append(self.x2[-1] + self.vx2*self.dt)
            self.y2.append(self.y2[-1] + self.vy2*self.dt)
        r2 = -self.y2[-2]/self.y2[-1]
        self.x2[-1] = (self.x2[-2] + r2*self.x2[-1])/(r2 + 1)
        self.y2[-1] = 0
        while(self.y3[-1] >= 0):
            Newv3 = math.sqrt(self.vx3**2 + self.vy3**2)
            self.vx3 = self.vx3 - ((1 - self.a*self.y3[-1]/self.T)**self.alpha)*self.B_m*Newv3*self.vx3*self.dt
            self.vy3 = self.vy3 - 9.8*self.dt - ((1 - self.a*self.y3[-1]/self.T)**self.alpha)*self.B_m*Newv3*self.vy3*self.dt
            self.x3.append(self.x3[-1] + self.vx3*self.dt)
            self.y3.append(self.y3[-1] + self.vy3*self.dt)
        r3 = -self.y3[-2]/self.y3[-1]
        self.x3[-1] = (self.x3[-2] + r3*self.x3[-1])/(r3 + 1)
        self.y3[-1] = 0
        while(self.y4[-1] >= 0):
            Newv4 = math.sqrt(self.vx4**2 + self.vy4**2)
            self.vx4 = self.vx4 - ((1 - self.a*self.y4[-1]/self.T)**self.alpha)*self.B_m*Newv4*self.vx4*self.dt
            self.vy4 = self.vy4 - 9.8*self.dt - ((1 - self.a*self.y4[-1]/self.T)**self.alpha)*self.B_m*Newv4*self.vy4*self.dt
            self.x4.append(self.x4[-1] + self.vx4*self.dt)
            self.y4.append(self.y4[-1] + self.vy4*self.dt)
        r4 = -self.y4[-2]/self.y4[-1]
        self.x4[-1] = (self.x4[-2] + r4*self.x4[-1])/(r4 + 1)
        self.y4[-1] = 0
        while(self.y5[-1] >= 0):
            Newv5 = math.sqrt(self.vx5**2 + self.vy5**2)
            self.vx5 = self.vx5 - ((1 - self.a*self.y5[-1]/self.T)**self.alpha)*self.B_m*Newv5*self.vx5*self.dt
            self.vy5 = self.vy5 - 9.8*self.dt - ((1 - self.a*self.y5[-1]/self.T)**self.alpha)*self.B_m*Newv5*self.vy5*self.dt
            self.x5.append(self.x5[-1] + self.vx5*self.dt)
            self.y5.append(self.y5[-1] + self.vy5*self.dt)
        r5 = -self.y5[-2]/self.y5[-1]
        self.x5[-1] = (self.x5[-2] + r5*self.x5[-1])/(r5 + 1)
        self.y5[-1] = 0
    def show_results(self):
        font = {'family': 'serif',
                'color':  'black',
                'weight': 'normal',
                'size': 15,
                }
        plot1, = pl.plot(self.x1, self.y1, 'r')
        plot2, = pl.plot(self.x2, self.y2, 'b')
        plot3, = pl.plot(self.x3, self.y3, 'g')
        plot4, = pl.plot(self.x4, self.y4, 'c')
        plot5, = pl.plot(self.x5, self.y5, 'y')
        pl.legend([plot1, plot2, plot3, plot4, plot5],['45$\degree$', '60$\degree$', '30$\degree$','50$\degree$', '40$\degree$'], loc = "best")
        pl.title('Both air drag and air density', fontdict = font)
        pl.xlabel('x asix(m)')
        pl.ylabel('y asix(m)')
        pl.savefig('chapter2_2.6.png',dpi=144)
        pl.show()
c = cannon()
c.run()
c.show_results()