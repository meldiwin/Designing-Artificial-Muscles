import numpy as np
import matplotlib.pyplot as plt
import time
import Sofa
import os
from math import *




class controller(Sofa.PythonScriptController):
        def initGraph(self, node):
            self.rootNode = node
            self.smawormNode= node.getChild('SMAWorm')
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
                    force=self.smawormNode.getObject('SMAForce').findData('forces').value
                    #if ( 0.02 <self.totalTime<0.021):
                        #d=self.smawormNode.getObject('Frame').findData('position').value
                        #D=d[4][2]
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
  
                    ### scalar force
                        Force= stress*A*1e6
                        force=[[0,0,Force[9],0,bending_stress[9],0], [0,0,Force[8], 0,bending_stress[8],0], [0,0,Force[7],0,bending_stress[7],0], [0,0,Force[6],0,bending_stress[6],0], [0,0,Force[5],0,bending_stress[5],0], [0,0,Force[4],0,bending_stress[4],0], [0,0,Force[3],0,bending_stress[3],0], [0,0,Force[2], 0,bending_stress[2],0], [0,0,Force[1],0,bending_stress[1],0], [0,0,Force[0],0,bending_stress[0],0]]
        
                        self.smawormNode.getObject('SMAForce').findData('forces').value= force
                        print force
                    
            
                    return force
          
                L=0.01 
                n=10
                dx=L/n;
                dt =0.0001
            

                force= solver_diffu(dx,dt)
               
                        