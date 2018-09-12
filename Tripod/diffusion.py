import numpy as np
import matplotlib.pyplot as plt
import time
import Sofa
import os
from math import *




class controller(Sofa.PythonScriptController):
        def initGraph(self, node):
            self.rootNode = node
            self.beamNode = node.getChild('beamMechanics')
            self.leg1Node= self.beamNode.getChild('leg1')
            self.leg2Node= self.beamNode.getChild('leg2')
            self.leg3Node= self.beamNode.getChild('leg3')
            self.mainNode = 2;
            self.notYetDone=True
            self.totalTime = 0
            self.file = open('position.txt', 'w') 
            
            
           
         

            
                
        #def onBeginAnimationStep(self,dt):
            #self.totalTime+=dt
            #force=self.smawormNode.getObject('SMAForce').findData('forces').value
            #print force
            #if ( 1.1 <self.totalTime<1.12):
                #d=self.smawormNode.getObject('Frame').findData('position').value
                #D=d[4][2]
               
               
        def onKeyPressed(self,c):
            if (ord(c)==20): 
                def solver_diffu(dx,dt):
                    self.totalTime+=dt
                    force= self.leg1Node.getObject('SMAForce_1').findData('forces').value
                    self.node.getObject('SerialPortBridgeGeneric').findData('size')= potentiometer1
                    self.node.getObject('SerialPortBridgeGeneric').findData('size')= potentiometer2
                    self.node.getObject('SerialPortBridgeGeneric').findData('size')= potentiometer3
                    
                    
                        #print D
               
                #L=0.01 
                #n=10
                    u0=0   
                    u0s=0
                    c=0.001
                    R=12e6
                    t_elapsed= 0.0001
                    Ke=9e9
                    A=2.167e-6
                    th_sq=6.25e-10
                    Young_Modulus=1e9
                #dx=L/n 
                    alpha=0.0002
                    t_final=0.2### two minutes 
                #dt =0.0001
                    b=2.167e-3
                    h= 2.5e-5
                    Inertia= (b*h**3)/12
                    x=np.linspace(dx, L, n)  
                    u=np.zeros(n)*u0
                    dudt=np.empty(n)  
                    u[0]=0;
                    for q in range(0, 2000):   
                        u[0]=u[0]+ 0.0005
                        u[0]=u[0]
                    

                        t= np.arange(0,self.totalTime,dt)
                        for j in range(0,len(t)):
                            for i in range(1,n-1):
                                dudt[i]= alpha*(-(u[i]-u[i-1])/dx**2+(u[i+1]-u[i])/dx**2) 
                        u=u+dudt*dt
                        u[n-1] = u[n-2];

        
                        q= c*u*(1-np.exp(-t_elapsed*alpha))
                        stress= (Ke*q**2)/(A* th_sq)
    
                    #q= (u*t_elapsed)/R 

                        bending_stress=  (Ke*q**2 * np.sin(89.9))/(A* th_sq) 
  
                        Moment_neutral= ((2*Inertia*bending_stress)/h)
    

    ### moment curvature
    ### dimensions in mm
                        Curvature= (Moment_neutral/(Young_Modulus* Inertia))* 1e3 
  
                    ### scalar force
                        Force= stress*A*1e6
                        
                        force=[[Force[0],0,0, 0,Moment_neutral[0],0], [Force[1],0,0, 0,Moment_neutral[1],0], [Force[2],0,0, 0,Moment_neutral[2],0], [Force[3],0,0, 0,Moment_neutral[3],0], [Force[4],0,0, 0,Moment_neutral[4],0], [Force[5],0,0,0 ,Moment_neutral[5],0], [Force[6],0,0, 0,Moment_neutral[6],0], [Force[7],0,0,0,Moment_neutral[7],0], [Force[8],0,0,0,Moment_neutral[8],0], [Force[9],0,0,0,Moment_neutral[9],0]]
        
        
        
                        self.leg1Node.getObject('SMAForce_1').findData('forces').value= force
                      
                    
            
                    return bending_stress, force
          
                L=0.01 
                n=10
                dx=L/n;
                dt =0.0001
            

                bending_stress, force = solver_diffu(dx,dt)
               
                
                def solver_diffu_2(dx_2,dt_2):
                    self.totalTime+=dt
                    force_2=self.leg2Node.getObject('SMAForce_2').findData('forces').value
                    #if ( 0.02 <self.totalTime<0.021):
                   
                        
                        
                #L=0.01 
                #n=10
                    u0_2=0   
                    u0s_2=0
                    c_2=0.001
                    R_2=12e6
                    t_elapsed_2= 0.0001
                    Ke=9e9
                    A_2=2.167e-6
                    th_sq_2=6.25e-10
                    Young_Modulus_2=1e9
                #dx=L/n 
                    alpha_2=0.0002
                    t_final_2=0.2### two minutes 
                #dt =0.0001
                    b_2=2.167e-3
                    h_2= 2.5e-5
                    Inertia_2= (b_2*h_2**3)/12
                    x_2=np.linspace(dx_2, L_2, n_2)  
                    u_2=np.zeros(n_2)*u0_2
                    dudt_2=np.empty(n_2)  
                    u_2[0]=0;
                    for q in range(0, 2000):   
                        u_2[0]=u_2[0]+ 0.0005
                        u_2[0]=u_2[0]
                    

                        t_2= np.arange(0,self.totalTime,dt_2)
                        for j in range(0,len(t_2)):
                            for i in range(1,n_2-1):
                                dudt_2[i]= alpha_2*(-(u_2[i]-u_2[i-1])/dx_2**2+(u_2[i+1]-u_2[i])/dx_2**2) 
                        u_2=u_2+dudt_2*dt_2
                        u_2[n_2-1] = u_2[n_2-2];

        
                        q_2= c_2*u_2*(1-np.exp(-t_elapsed_2*alpha_2))
                        stress_2= (Ke*q_2**2)/(A_2* th_sq_2)
    

                        bending_stress_2=  (Ke*q_2**2 * np.sin(89.9))/(A_2* th_sq_2) 
                        
                          ### dimensions in m
    
                        Moment_neutral_2= ((2*Inertia_2*bending_stress_2)/h_2)
    


                        Curvature_2= (Moment_neutral_2/(Young_Modulus_2* Inertia_2))* 1e3 
  
                    ### scalar force
                        Force_2= stress_2*A_2*1e6
                        force_2=[[Force_2[0],0,0, 0,Moment_neutral_2[0],0], [Force_2[1],0,0, 0,Moment_neutral_2[1],0], [Force_2[2],0,0, 0,Moment_neutral_2[2],0], [Force_2[3],0,0, 0,Moment_neutral_2[3],0], [Force_2[4],0,0, 0,Moment_neutral_2[4],0], [Force_2[5],0,0,0 ,Moment_neutral_2[5],0], [Force_2[6],0,0, 0,Moment_neutral_2[6],0], [Force_2[7],0,0,0,Moment_neutral_2[7],0], [Force_2[8],0,0,0,Moment_neutral_2[8],0], [Force_2[9],0,0,0,Moment_neutral_2[9],0]]
        
                        self.leg2Node.getObject('SMAForce_2').findData('forces').value= force_2
                        print force_2
                        
                         
                    d=self.beamNode.getObject('MO').findData('position').value
                  
                    D_0=d[1][3]  # curvature at  first leg the tip, z direction
                    D_1=d[10][3] # curvature at the clamping, z direction
                    D_2=d[11][3]  # curvature at the second leg
                    D_3=d[20][3]  # curvature at the second leg
                    D_4=d[21][3]  # curvature at the second leg
                    D_5=d[30][3]
                        
                    print 'D_0 is: ', D_0
                    print 'D_1 is: ', D_1
                    print 'D_2 is: ', D_2
                    print 'D_3 is: ', D_3  
                    print 'D_4 is: ', D_4
                    print 'D_5 is: ', D_5
                    
            
                    return bending_stress_2, force_2
          
                L_2=0.01 
                n_2=10
                dx_2=L_2/n_2;
                dt_2=0.0001
            

                bending_stress_2, force_2 = solver_diffu_2(dx_2,dt_2)
                        