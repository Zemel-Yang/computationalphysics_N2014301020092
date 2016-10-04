import pylab as pl
class uranium_decay:
     def __init__(self,number_of_a = 100, number_of_b = 0,time_constant = 1, time_of_duration = 5, time_step = 0.05):
         # unit of time is second
         self.nuclei_a = [number_of_a]
         self.nuclei_b = [number_of_b]
         self.t = [0]
         self.tau = time_constant
         self.dt = time_step
         print("Initial number of nuclei ->", number_of_a)
         print("Time constant ->", time_constant)
         print("time step -> ", time_step)
         print("total time -> ", time_of_duration)
     def calculate(self):
        for i in range(100):
           tmpa = self.nuclei_a[i] + (self.nuclei_b[i] - self.nuclei_a[i]) / self.tau * self.dt
           self.nuclei_a.append(tmpa)
           tmpb = self.nuclei_b[i] + (self.nuclei_a[i] - self.nuclei_b[i]) / self.tau * self.dt
           self.nuclei_b.append(tmpb)
           self.t.append(self.t[i] + self.dt)
     def store(nuclei_a,nuclei_b,t):
           data = open('data.txt','w')
           for i in range(100):
               data.write(str(t[i]))
               data.write(' ')
               data.write(str(nuclei_a[i]))
               data.write(' ')
               data.write(str(nuclei_b[i]))
               data.write('\n')
               data.close
     def show_results(self):
       plot1, = pl.plot(self.t,self.nuclei_a,'g')
       plot2, = pl.plot(self.t,self.nuclei_b,'r')
       pl.xlabel('Time(s)')
       pl.ylabel('Number of Nuclei')
       pl.legend([plot1, plot2], ['NA', 'NB'], loc="best")
       pl.xlim(0, 5)
       pl.ylim(0, 100)
       pl.savefig('chapter1_1.5.png',dpi=144)
       pl.show()
b = uranium_decay()
b.calculate()
b.show_results()