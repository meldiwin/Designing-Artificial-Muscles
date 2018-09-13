import numpy as np
import matplotlib.pyplot as plt
import time
import serial
from time import sleep


L=0.01 # the length of the actuator
n=10# number of spatial samples


u0=0   # s

u0s=0### the voltage before the clamping at t is zero
#### the final value that voltage will reach at the space
c=0.0009
R=12e6
t_elapsed= 0.0001
Ke=9e9
A=2.167e-6
th_sq=6.25e-10

t_e= 0.00015
dx=L/n  ### space step
alpha=0.00017# the inverse of tau (real value)
#0.0002# time step
t_final=0.2### two minutes 
dt= 0.0001
b=2.167e-3
h= 2.5e-5

#### dimensions in meter

Inertia= (b*h**3)/12

#### flexure rigidity
Young_Modulus= (12*4.1*(0.0063)**3)/(3*2.167e-3*(2.5e-5)**3)




x=np.linspace(dx, L, n)  ### space


u=np.zeros(n)*u0
dudt=np.empty(n)  ### empty vector


f= open("voltage.txt",'w')
    
u[0]=0


for q in range(0, 2000): ### to generate 1 volt  
    u[0]=u[0]+ 0.0009## sampling rate
    u[0]=u[0]
    #print u[0]
    t= np.arange(0,t_final,dt)# iteration
    for j in range(0,len(t)):
        plt.clf()
        
        for i in range(1,n-1):  
            dudt[i]= alpha*(-(u[i]-u[i-1])/dx**2+(u[i+1]-u[i])/dx**2) 
    u=u+dudt*dt
    u[n-1] = u[n-2];
    
    
    

  
    q_e= (u/R)* t_e
 
   
    q_i= c*u*(1-np.exp(-t_elapsed*alpha))
 
   
    

    stress= (Ke*q_i * q_e)/(A* th_sq)
    
    
    ## add bonding angle
    
    bending_stress=  (Ke*q_i * q_e * np.sin(89.9))/(A* th_sq) 
    


    Force= stress*A*1e6
    

    
    epsilon= bending_stress/Young_Modulus
    

    
    dl= dx* epsilon
   
  
   
    
    #print dl

    Moment_neutral= ((2*Inertia*bending_stress)/h)
  
    Curvature= (Moment_neutral/(Young_Modulus* Inertia))* 1e3
    
    print Curvature
    