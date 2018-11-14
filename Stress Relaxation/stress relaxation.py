import numpy as np
import matplotlib.pyplot as plt
import time
from time import sleep


L=0.01 # the length of the actuator
n=10# number of spatial samples


u0=0  

u0s=0### the voltage before the clamping at t is zero
#### the final value that voltage will reach at the space
c=0.0009
R=12e6
t_elapsed= 0.0001
Ke=9e9
A=2.167e-6
th_sq=6.25e-10


  
### Design Stiffness

#R= 0.2  # desired curvature at the tip
#K=   # desired stiffness at the tipforc

#F=k* R  # applied external force
    
    
    
#### young modulus    
    
Young_Modulus= (12*4.1*(0.0063)**3)/(3*2.167e-3*(2.5e-5)**3)
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



x=np.linspace(dx, L, n)  ### space


u=np.zeros(n)*u0
dudt=np.empty(n)  ### empty vector


f= open("tipforce.txt",'w')
    
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
    
    
    

    u_0=1;
    ## the resistance of the conductive layer
    r_0=0.25
    
    I_0= u_0/r_0
    q_e= (u_0/r_0)* t_e
     
  
    Time=0.0001;
    #q_i= (c*u* Time*alpha)*(np.exp(-t_elapsed*alpha))
    
    ## discharging
    q_i= (c* Time*alpha)*(np.exp(t_elapsed*alpha))* u;
    
    ## charging
    #q_i= (c* Time*alpha)*(1-np.exp(t_elapsed*alpha))* u;
    
    
  
  
    #normal stress
    stress= (Ke*q_i**2)/(A* th_sq)
    
    
    # axial stress
    bending_stress=  (Ke*q_i**2* np.sin(89.9))/(A* th_sq) 
    

    
    
    #### axial force
    Force= stress*A*1e6
    #print (Force[9])
    #f.write( str(Force[9]) + "\n")

    
    
    epsilon_x= (bending_stress/Young_Modulus)
    #print(epsilon_x)
     
    epsilon_z= (stress/Young_Modulus)
    
       
    ########### finding the strain at specific point of time
   
    #eta=   ## viscosity
    #the relaxation time
    #tau= eta/Young_Modulus
    
    tau=0.1 # this value is verified with the original value of epsilon
    # viscosity
    eta= tau* Young_Modulus
    
    print(eta)
    
    # the time that is required to be measured at
    time=0.2
     
     
    epsilon_x_e= (bending_stress/Young_Modulus)*(1-np.exp(-time/tau))
    
    #print(epsilon_x_e)
    
    epsilon_z_e= (stress/Young_Modulus)*(1-np.exp(-time/tau))
    
  
     #normal (thickness)
    dl= dx* epsilon_z
    
    # axial (length)
    dl_1= dx*epsilon_x
    
    h_final= h+ dl
    l_final=L+ dl_1
    
    
    k=4.1; # the stiffness at point 6.3 from the clamping point, the stiffness and the electric conductivity changes 
    Young_Modulus_e= (12*4.1*(0.0063+dl_1)**3)/(3*2.167e-3*(2.5e-5+ dl)**3)
    
    #print (Young_Modulus_e)


    
    
   
    
    # The current density, first we assume that the thickness is uniform along the spatial domain 
    J= I_0/(h_final* b)
    
    
    # The electric field
    E=u_0/(dx+dl)
    #print(E)
    
    # the electric conductivity, dimensions in cm
    sigma= (J/(E*1e2))
    #print (sigma)


    
    Moment_neutral= ((2*Inertia*bending_stress)/h)
    


    ### dimensions in mm
    Curvature= (Moment_neutral/(Young_Modulus* Inertia))* 1e3
    
    ## deflection in the normal direction
    z= epsilon_x/Curvature
    #print(z)
    
    ## radius of curvature  (check)
    
    rho= epsilon_x/z
    
    #print(rho)
    
    
    #print(Curvature)
    
    
    #### Twisting Moment
    
    
  
    
    
 
    
    
    
    
