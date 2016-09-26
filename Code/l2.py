import time
import os
a=("   ############\n")
b=("   ###      ###\n")
c=("       ####    \n")
d=("##################\n")
e=("        ##        \n")
f=("#####   ##  ######\n")
k=("    #########   ##\n")
g=3*a+6*b+2*c+2*d+2*c+2*a+4*b
h=3*e+3*f+4*k+3*f+3*e
i=4*b+2*a+2*c+2*d+2*c+6*b+3*a
j=3*e+3*f+4*k+3*f+3*e
li=[g,h,i,j]
i=0
while i<20:
    print(li[i%4])
    time.sleep(1)
    i=i+1
    os.system('cls')