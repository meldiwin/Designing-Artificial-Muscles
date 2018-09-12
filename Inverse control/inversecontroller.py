import numpy as np
import matplotlib.pyplot as plt
import time
import Sofa
import os
from math import *




class controller(Sofa.PythonScriptController):
        def initGraph(self, node):
            self.rootNode = node
            self.beamNode= node.getChild('beamMechanics')
            #self.leg1Node= self.beamNode.getChild('leg1')
            #self.leg2Node= self.beamNode.getChild('leg2')
            #self.leg3Node= self.beamNode.getChild('leg3')
            self.mainNode = 2;
            self.notYetDone=True
            self.totalTime = 0
            self.file = open('position.txt', 'w')  
            
            
               
        def onKeyPressed(self,c):
            if (ord(c)==20):                
                #self.totalTime+=dt
                force=self.beamNode.getObject('MO').findData('force').value
                
                #print len(force)
               
               
                Force_1= force[10]
                print Force_1[5]*1e3
                print Force_1[2]*1e6
                Force_2= force[30]
                print Force_2[5]*1e3
                print Force_2[2]*1e6
                Force_3= force[20]
                print Force_3[5]*1e3
                print Force_3[2]*1e6
                
        
              
            

                        
            ### compute curvature at the tip and at the clamping 
                d=self.beamNode.getObject('MO').findData('position').value
                D_0=d[1][3]  # curvature at  first leg the tip, z direction
                D_1=d[10][3] # curvature at the clamping, z direction
                D_2=d[11][3]  # curvature at the second leg
                D_3=d[20][3]  # curvature at the second leg
                D_4=d[21][3]  # curvature at the second leg
                D_5=d[30][3]  # curvature at the second leg
 
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
                Young_Modulus= (12*4.1*(0.0063)**3)/(3*2.167e-3*(2.5e-5)**3)
                alpha_u=0.00003

                    
                
                Force=1000
                    #### convert dimensions in to mm
                u_1 = ((-1*Force_1[2]*th_sq )/(Ke*(c*(1-np.exp(-t_elapsed*alpha_u)))**2))**0.5
                
                print " u_1 is : ", u_1
                u_2 = ((Force_2[2]*th_sq )/(Ke*(c*(1-np.exp(-t_elapsed*alpha_u)))**2))**0.5
                
                print " u_2 is : ", u_2
                
                u_3 = ((Force_3[2]*th_sq )/(Ke*(c*(1-np.exp(-t_elapsed*alpha_u)))**2))**0.5
                
                print " u_3 is : ", u_3                    
                    #### Or using moment
                    #u = ((M*th_sq*h*A )/(2*Inertia(Ke*(c*(1-np.exp(-t_elapsed*alpha_u)))**2)))**0.5
                    
                    #self.beamNode.getObject('SerialPortBridgeGeneric').findData('size').value = u
                    
                    #https://www.youtube.com/watch?v=L9TeiCDrXU4
                    
                    
                    ### send u to the physical world
                    
                    
                    
                        #if ( 0.02 <self.totalTime<0.021):
                        #d=self.smawormNode.getObject('Frame').findData('position').value
                        #D=d[4][2]
                        #print D
                    
            # send moment at the clamping node or tip node and compute u directly or use the diffusion model to compute u at the tip for verification
                    
            #self.node.getObject('SerialPortBridgeGeneric').findData('size')= force
                    