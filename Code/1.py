# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 21:33:14 2016

@author: admin12
"""

import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
from scipy.fftpack import rfft, irfft, fftfreq

class Guass_seidel:
    def __init__(self,L,dx,T,e):
        self.L = L
        self.dx = dx
        self.r = 0.25
        self.c = 300
        self.T = T
        self.dt = self.dx/(4*self.c)
        self.e = e #epsilon
        pass
    
    def initialization(self):
        self.string = []
        for i in range(int(self.T/self.dt)):
            self.string.append([])
            for j in range(int(self.L/self.dx)):
                self.string[i].append(0)
        '''
        x_0 = int((self.L/self.dx)/8)
        self.string[1][x_0] = 0.1
        k1 = 0.1/(x_0 - 1)
        k2 = 0.1/(int(self.L/self.dx) - 1 - x_0)
        for l in range(1,x_0):
            self.string[1][l] = k1*(l - 1)
        for m in range(x_0,int(self.L/self.dx) - 1):
            self.string[1][m] = 0.1 - k2*(m - x_0)
        self.string[1][0] = -self.string[1][2]
        self.string[1][-1] = -self.string[1][-3]
        #plt.plot(self.string[1])
        self.string[0] = self.string[1][:]
        '''
        
        for l in range(1,int(int(self.L/self.dx)) - 1):
            self.string[0][l] = np.sin(10*np.pi/(48.5)*(l - 1))
            self.string[1][l] = np.sin(10*np.pi/(48.5)*(l - 1))
        self.string[0][0] =  - self.string[0][2]
        self.string[0][-1] = - self.string[0][-3]
        self.string[1][0] =  - self.string[1][2]
        self.string[1][-1] = - self.string[1][-3]
        #plt.plot(self.string[1])
        #print self.string[1]
        
        '''
        for l in range(1,int(int(self.L/self.dx) - 1)):
            self.string[0][l] = np.e**(-0.1*(l - 30)**2) 
        self.string[0][1] = 0
        self.string[0][-2] = 0
        self.string[0][0] =  - self.string[0][2]
        self.string[0][-1] = - self.string[0][-3]
        self.string[1] = self.string[0][:]
        #plt.plot(self.string[1])
        '''
        
        return 0
        
    def calculation(self):
        print 1
        M = int(self.L/self.dx)
        for i in range(2,int(self.T/self.dt)):
            for j in range(2,M-2):
                self.string[i][j] = (2 - 2*self.r**2 - 6*self.e*self.r**2*M**2)*self.string[i - 1][j] - self.string[i - 2][j] + self.r**2*(1 + 4*self.e*M**2)*(self.string[i-1][j+1]+self.string[i-1][j-1]) - self.e*self.r**2*M**2*(self.string[i-1][j+2]+self.string[i-1][j-2])
                #self.string[i][j] = 2*(1-self.r**2)*self.string[i - 1][j] - self.string[i - 2][j] + self.r**2*(self.string[i - 1][j + 1] +self.string[i - 1][j - 1])
                self.string[i][0] = -self.string[i][2]
                self.string[i][-1] = -self.string[i][-3]
        #print self.string 
        #plt.plot(self.string[-1])
        return self.string
        
    def fft(self):
        t_plot = np.arange(0,self.T,self.dt)
        print len(t_plot)
        amplitude_record = []
        for i in range(int(self.T/self.dt)):
            amplitude_record.append(self.string[i][20])
        print len(amplitude_record)
        '''
        plt.subplot(121)
        plt.title('String signal versus time')
        plt.ylabel('Signal (arbitrary units)')
        plt.xlabel('Time (s)')
        plt.plot(t_plot,amplitude_record)
        '''
        freq = fftfreq(len(amplitude_record), d=self.dt)
        freq = np.array(abs(freq))
        f_signal = rfft(amplitude_record)
        f_signal = np.array(f_signal**2)
        #plt.subplot(122)
        plt.title('Power spectra')
        plt.ylabel('Power (arbitrary units)')
        plt.xlabel('Frequency (Hz)')
        plt.xlim(2000,8000)
        plt.plot(freq,f_signal,label = 'epsilon = '+str(self.e))
        return 0
    

    
plt.figure(figsize = (8,8))    
A = Guass_seidel(1,0.01,0.05,0)
A.initialization()
data_record = A.calculation()
A.fft()

B = Guass_seidel(1,0.01,0.05,1e-5)
B.initialization()
data_record = B.calculation()
B.fft()
C = Guass_seidel(1,0.01,0.05,2e-5)
C.initialization()
data_record = C.calculation()
C.fft()
plt.legend()
plt.savefig('chapter6_6.16_highsine_c.png',dpi = 144)
plt.show()

'''
# ---- animation ---------------------------------
fig = plt.figure(figsize = (8,6))
ax = plt.axes(xlim=(0, 1),ylim = (-1,1))
line, = ax.plot([], [], 'k')
def init():
    line.set_data([], [])
    return line,
    
def animate(i):
    x_plot = np.arange(0.01,0.99,0.01)
    y_plot = []
    for j in range(1, int(A.L/A.dx) - 1):
        y_plot.append(data_record[i][j])
    line.set_data(x_plot,y_plot)
    return line,
        
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=100, interval=50, blit=True)
anim.save('chapter6_string_guass_e.gif', fps=20, writer='Feng_Chen')
plt.show()
'''