import numpy as np
import matplotlib.pyplot as plt
import time
import serial
from time import sleep






############################### enter the position of each actuator workspace
    
    
a = input("enter the coordinates of actuator(a) tip: ")
b= input("enter the coordinates of actuator(b) tip: ")
c= input("enter the coordinates of actuator(c) tip: ")
G= input("enter the coordinates of point G: ")
G_n= input("enter the coordinates of point G_n': ")



################## constraints

## strain

## curvature


########################################## first actuator


L_1=0.01 # the length of the actuator
n_1=10# number of spatial samples
u0_1=0   # s
u0s_1=0### the voltage before the clamping at t is zero
#### the final value that voltage will reach at the space
c_1=0.0009
R_1=12e6
t_elapsed_1= 0.0001
Ke=9e9
A_1=2.167e-6
th_sq_1=6.25e-10
t_e_1= 0.00015
dx_1=L_1/n_1  ### space step
alpha_1=0.00017# the inverse of tau (real value)
#0.0002# time step
t_final_1=0.2### two minutes 
dt_1= 0.0001
b_1=2.167e-3
h_1= 2.5e-5

Inertia_1= (b_1*h_1**3)/12

#### flexure rigidity
Young_Modulus_1= (12*4.1*(0.0063)**3)/(3*2.167e-3*(2.5e-5)**3)




x_1=np.linspace(dx_1, L_1, n_1)  ### space


u_1=np.zeros(n_1)*u0_1
dudt_1=np.empty(n_1)  ### empty vector


    
u_1[0]=0


### here we define the amplitude of the voltage signal 
# number of samples for the sampled source voltage before entering the sample
for q in range(0, 2000): ### to generate 1 volt  
    u_1[0]=u_1[0]+ 0.0009## sampling rate
    u_1[0]=u_1[0]
    #print u[0]
    t_1= np.arange(0,t_final_1,dt_1)# iteration
    for j in range(0,len(t_1)):
        plt.clf()
        
        for i in range(1,n_1-1):  
            dudt_1[i]= alpha_1*(-(u_1[i]-u_1[i-1])/dx_1**2+(u_1[i+1]-u_1[i])/dx_1**2) 
    u_1=u_1+dudt_1*dt_1
    u_1[n_1-1] = u_1[n_1-2];
    

  
    q_e_1= (u_1/R_1)* t_e_1
 
   
    q_i_1= c_1*u_1*(1-np.exp(-t_elapsed_1*alpha_1))
 
   
    #stress= (Ke*q**2)/(A* th_sq)
    stress_1= (Ke*q_i_1 * q_e_1)/(A_1* th_sq_1)
    
    
    
    bending_stress_1=  (Ke*q_i_1 * q_e_1* np.sin(89.9))/(A_1* th_sq_1) 

    Force_1= stress_1*A_1*1e6

    
    epsilon_1= bending_stress_1/Young_Modulus_1
    
    ''' defining the constraints of the tripod  the strain and the curvature'''  
    

    dl_1= dx_1* epsilon_1
   
    
    Moment_neutral_1= (Inertia_1*bending_stress_1)/h_1    
    ### moment curvature
    Curvature_1= Moment_neutral_1/(Young_Modulus_1* Inertia_1)
    
    
    
    ######################################## The second actuator################################
    
    
L_2=0.01 # the length of the actuator
n_2=10# number of spatial samples


u0_2=0   # s

u0s_2=0### the voltage before the clamping at t is zero
#### the final value that voltage will reach at the space
c_2=0.0009
R_2=12e6
t_elapsed_2= 0.0001
Ke=9e9
A_2=2.167e-6
th_sq_2=6.25e-10

t_e_2= 0.00015
dx_2=L_2/n_2  ### space step
alpha_2=0.00017# the inverse of tau (real value)
#0.0002# time step
t_final_2=0.2### two minutes 
dt_2= 0.0001
b_2=2.167e-3
h_2= 2.5e-5

Inertia_2= (b_2*h_2**3)/12

#### flexure rigidity
Young_Modulus_2= (12*4.1*(0.0063)**3)/(3*2.167e-3*(2.5e-5)**3)




x_2=np.linspace(dx_2, L_2, n_2) 


u_2=np.zeros(n_2)*u0_2
dudt_2=np.empty(n_2) 


    
u_2[0]=0

for q in range(0, 2000): ### to generate 1 volt  
    u_2[0]=u_2[0]+ 0.0009## sampling rate
    u_2[0]=u_2[0]
    #print u[0]
    t_2= np.arange(0,t_final_2,dt_2)# iteration
    for j in range(0,len(t_2)):
        plt.clf()
        
        for i in range(1,n_2-1):  
            dudt_2[i]= alpha_2*(-(u_2[i]-u_2[i-1])/dx_2**2+(u_2[i+1]-u_2[i])/dx_2**2) 
    u_2=u_2+dudt_2*dt_2
    u_2[n_2-1] = u_2[n_2-2];
    
    
    

    
  

  
    q_e_2= (u_2/R_2)* t_e_2
 
   
    q_i_2= c_2*u_2*(1-np.exp(-t_elapsed_2*alpha_2))
 
   
    
  
  
    #stress= (Ke*q**2)/(A* th_sq)
    stress_2= (Ke * q_i_2 * q_e_2)/(A_2* th_sq_2)
    
    
    
    bending_stress_2=  (Ke*q_i_2 * q_e_2 * np.sin(89.9))/(A_2* th_sq_2) 
    

    
    
                    #### axial force
    Force_2= stress_2*A_2*1e6

    
    epsilon_2= bending_stress_2/Young_Modulus_2
    
    ''' defining the constraints of the tripod  the strain and the curvature'''  
    
    
    dl_2= dx_2* epsilon_2   
  


    Moment_neutral_2= (Inertia_2*bending_stress_2)/h_2
    
    ### moment curvature
    Curvature_2= Moment_neutral_2/(Young_Modulus_2* Inertia_2)


    ############################# The third actuator #########################################
    
    
    
L_3=0.01 # the length of the actuator
n_3=10# number of spatial samples


u0_3=0   # s

u0s_3=0### the voltage before the clamping at t is zero
#### the final value that voltage will reach at the space
c_3=0.0009
R_3=12e6
t_elapsed_3= 0.0001
Ke=9e9
A_3=2.167e-6
th_sq_3=6.25e-10

t_e_3= 0.00015
dx_3=L_3/n_3  ### space step
alpha_3=0.00017# the inverse of tau (real value)
#0.0002# time step
t_final_3=0.2### two minutes 
dt_3= 0.0001
b_3=2.167e-3
h_3= 2.5e-5

Inertia_3= (b_3*h_3**3)/12

#### flexure rigidity
Young_Modulus_3= (12*4.1*(0.0063)**3)/(3*2.167e-3*(2.5e-5)**3)




x_3=np.linspace(dx_3, L_3, n_3)  ### space


u_3=np.zeros(n_3)*u0_3
dudt_3=np.empty(n_3)  ### empty vector



    
u_3[0]=0


### here we define the amplitude of the voltage signal 
# number of samples for the sampled source voltage before entering the sample
for q in range(0, 2000): ### to generate 1 volt  
    u_3[0]=u_3[0]+ 0.0009## sampling rate
    u_3[0]=u_3[0]
    #print u[0]
    t_3= np.arange(0,t_final_3,dt_3)# iteration
    for j in range(0,len(t_3)):
        plt.clf()
        
        for i in range(1,n_3-1):  
            dudt_3[i]= alpha_3*(-(u_3[i]-u_3[i-1])/dx_3**2+(u_3[i+1]-u_3[i])/dx_3**2) 
    u_3=u_3+dudt_3*dt_3
    u_3[n_3-1] = u_3[n_3-2];
    


  
    q_e_3= (u_3/R_3)* t_e_3
 
   
    q_i_3= c_3*u_3*(1-np.exp(-t_elapsed_3*alpha_3))
 
   
    
  
  
    #stress= (Ke*q**2)/(A* th_sq)
    stress_3= (Ke * q_i_3 * q_e_3)/(A_3* th_sq_3)
    
    
    
    bending_stress_3=  (Ke*q_i_3 * q_e_3 * np.sin(89.9))/(A_3* th_sq_3) 
    

    Force_3= stress_3*A_3*1e6

    
    
    epsilon_3= bending_stress_3/Young_Modulus_3
    
    ''' defining the constraints of the tripod  the strain and the curvature'''  
    
    
    dl_3= dx_3* epsilon_3   
  

    
    Moment_neutral_3= (Inertia_3*bending_stress_3)/h_3
  
    Curvature_3= Moment_neutral_3/(Young_Modulus_3* Inertia_3)
    
    


############### constraints

### max(both direct)

 d_max= dl_1+ dl_2+ dl_3
 
 print d_max
 
 Curvature_max= Curvature_1 + Curvature_2 + Curvature_3
 
 print Curvature_max
 
 
 
 ### mini
 
 
 
 
 
 
 
############################## compute d

#### extract x,y
d_x,y= G_n - G

### extract z

d_z=

######## condition for checking the workspace constraints
    

if (d_x,y> d_max) and (d_z> Curvature_max):
    print error

elif (d_x,y> d_max) and (d_z <= Curvature_max):
    print error
    
elif (d_x,y <=d_max) and (d_z > Curvature_max):
    print error
    
else (d_x,y <=d_max) and (d_z <= Curvature_max):
    print ('d is correct')
    
    
    
##### compare the new point of G with each actuator tip coordinates and select the shortest path

d_1= d_x,y- a_x,y;
d_2= d_x,y- b_x,y;
d_3= d_x,y- a_x,y;

#### checking curvature
C_a= d_z
##### add curvature and condition
if (d_1 < d_2):
    print ('compare d_1 with d_3')
elif (d_1 < d_3):
    print ('select d_1')
elif (d_2 < d_3):
    print ('compare  d_2 with d_1')
elif (d_2 < d_1):
    print ('select  d_2')
elif (d_3 < d_2):
    print ('compare  d_3 with d_1')
elif (d_3 < d_1):
    print ('select  d_3')
    
    
    



####### actuated the shortest path


#### compute the new strain and curvature and the stress


######## update the location of the actuators by adding stress

delta= ##### the compute strain from the selected actuator
C= # the computed curvature from the selected actuator

### we cannot add strain, so we compute stress at the selected shortest path of the actuator

### in that case we assume that the other actuators are not activated
stress_a= [];
stress_b_n= stress_a+ stress_b;
stress_c_n=stress_a+ stress_c;

##### compute the updated locations of each actuator from the stress 


#### having actuation between each stress with strain and curvature

#### update locations
 
Curvature_max= Curvature_1 + Curvature_2 + Curvature_3
 
 print Curvature_max
 
 
 
 
 #### compute d again with the updated locations
 
 
 #### conditions
 
 
 
 #### select the shortest path
 
 
 
 #### compute stress again
 
 
 




    
    
    
    
    
    
 
 