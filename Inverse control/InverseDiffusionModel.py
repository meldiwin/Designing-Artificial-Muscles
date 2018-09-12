import numpy as np
import matplotlib.pyplot as plt
import time
import serial
from time import sleep


L=0.01 
n=10

sigma0=0  

sigma0s=0
c=0.0009
R=12e6
t_elapsed= 0.0006
Ke=9e9
A=2.167e-6
th_sq=6.25e-10

t_e= 0.00015
dx=L/n  


alpha=0.00009# the inverse of tau (real value)




t_final=0.2### two minutes 
dt= 0.0001
b=2.167e-3
h= 2.5e-5

Inertia= (b*h**3)/12

#### flexure rigidity
Young_Modulus= (12*4.1*(0.0063)**3)/(3*2.167e-3*(2.5e-5)**3)

alpha_u=0.00003



x=np.linspace(dx, L, n) 


sigma=np.zeros(n)*sigma0
dsigmadt=np.empty(n)  


f= open("voltage.txt",'w')
    
sigma[0]=0


for q in range(0, 2100):   
    sigma[0]=sigma[0]+ 1
    sigma[0]=sigma[0]
   
    t= np.arange(0,t_final,dt)
    for j in range(0,len(t)):
        
        
        for i in range(1,n-1):  
            dsigmadt[i]= alpha*(-(sigma[i]-sigma[i-1])/dx**2+(sigma[i+1]-sigma[i])/dx**2) 
    sigma=sigma+dsigmadt*dt
    sigma[n-1] = sigma[n-2];
    
    
    
    
    

    u = ((sigma*th_sq*A )/(Ke*(c*(1-np.exp(-t_elapsed*alpha_u)))**2))**0.5
    
    u = ((F*th_sq )/(Ke*(c*(1-np.exp(-t_elapsed*alpha_u)))**2))**0.5
    u = ((M*th_sq*h*A )/(2*Inertia(Ke*(c*(1-np.exp(-t_elapsed*alpha_u)))**2)))**0.5
        
    print u

  
    
   