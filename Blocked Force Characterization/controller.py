import Sofa
import os
from math import sin, pi
from time import gmtime, strftime
import numpy
import sys
from math import *
from math import cos, exp, pi
from scipy.integrate import quad
import scipy.integrate as integrate
import scipy.special as special
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
import matplotlib.pyplot as plto

####Generate a test signal, a 2 Vrms sine wave at 1234 Hz
#fs = 10e3
#N = 1e5
#amp = 2*np.sqrt(2)
#freq = 1234.0
#noise_power = 0.001 * fs / 2
#time = np.arange(N) / fs
#x = amp*np.sin(2*np.pi*freq*time)
#x += np.random.normal(scale=np.sqrt(noise_power), size=time.shape)




#### Model Parameters
#D=    #Diffusion coefficient
#h =  #th1=self.cpUpNode.getObject('Interpol').findData('lengthZ').value   # Thickness of the PPy layer
#R=  #Electrolyte and contact resistance
#delta = #Thickness of double-layer capacitance
#I = #Current
#V = #Input voltage
#C=  # Double-layer capacitance
#Z_D=  #Diffusion impedance
#alpha=  #strain charge ratio
#sigma =   alpha * E2* rho # induced stress by charges
#rho = I/W*10.716*th1# charge density
#W= self.speNode.getObject('Interpol').findData('lengthY').value

##### input
#for t in range(0,2000)
#r(t) = 0.5*sin(pi*t)+0.5*sin(0.2*pi*t)







class controller(Sofa.PythonScriptController):


    def initGraph(self, node):
         
            self.rootNode = node
            self.smawormNode= node.getChild('SMAWorm')
            self.cpUpNode= self.smawormNode.getChild('CP_up')
            self.cpDownNode= self.smawormNode.getChild('CP_down')
            self.speNode= self.smawormNode.getChild('SPE')
            self.Point=self.smawormNode.getChild('SMAPoint')
            self.mainNode = 2;
            self.notYetDone=True
            self.totalTime = 0
            self.result = integrate.quad(lambda x: special.jv(2.5,x), 0, 4.5)
            print self.result
            self.file = open('position.txt', 'w')    #  position of  pedot up layer
            
    
    # function we want to integrate
    


    def onBeginAnimationStep(self,dt):
        self.totalTime+=dt
        lengths_up = self.cpUpNode.getObject('Interpol').findData('lengthList').value
        lengths_down = self.cpDownNode.getObject('Interpol').findData('lengthList').value
        E1 = self.speNode.getObject('Interpol').findData('defaultYoungModulus').value
        E2 = self.cpUpNode.getObject('Interpol').findData('defaultYoungModulus').value
        E3 = self.cpDownNode.getObject('Interpol').findData('defaultYoungModulus').value
        position=self.smawormNode.getObject('Frame').findData('position').value
        force=self.smawormNode.getObject('Frame').findData('force').value
        velocity=self.smawormNode.getObject('Frame').findData('velocity').value
        
        
        
        W= self.speNode.getObject('Interpol').findData('lengthY').value
        th1=self.cpUpNode.getObject('Interpol').findData('lengthZ').value
        th2=self.cpDownNode.getObject('Interpol').findData('lengthZ').value
        th3=self.speNode.getObject('Interpol').findData('lengthZ').value
        th=th1+ th2+th3
        delta= th2+th3
    
       

        
        L=10.716;
        DL_1 = 0.0000972;
        #DL_1 = 0.00008332;  # this is analogy of the voltage  value for each test mapping 
        numLengthUp = 3;
        length_up=0.0; 
        
        
        for i in range(numLengthUp):
            length_up = length_up + lengths_up[i][0]  
            
            
            
            dl_up=[0]*numLengthUp;  
            
            
            
        for i in range(numLengthUp):
            dl_up[i] =  DL_1*lengths_up[i][0]/length_up; 
            
           # print dl_up[i]
            
            
            
            ''' Time here is critical '''
        if (self.totalTime <= 4): 
            
            for i in range(numLengthUp):
                lengths_up[i][0] = lengths_up[i][0] + dl_up[i];
                self.cpUpNode.getObject('Interpol').findData('lengthList').value = lengths_up;  # replacing the lengthlist in SOFA scene with the new value of lengths_up
                
                
                
            for i in range(numLengthUp):
                lengths_down[i][0] = lengths_down[i][0] - dl_up[i];
                self.cpDownNode.getObject('Interpol').findData('lengthList').value = lengths_down;            
                self.file.write(str(self.totalTime) + ", " + str(self.smawormNode.getObject("Frame").position)+"\n")
                self.file.write(str(self.totalTime) + ", " + str(self.smawormNode.getObject("Frame").force)+"\n")
                self.file.write(str(self.totalTime) + ", " + str(self.smawormNode.getObject("Frame").velocity)+"\n")
                
        if ( 1.11<self.totalTime<1.12):
            d=self.Point.getObject('location').findData('position').value
            D=d[0][2]
            print 'D is ', D
            L_down=lengths_down[i][0]*50
            L_up=lengths_up[i][0]*50
            print 'length is', lengths_down[i][0]*50
            R= (L_up**2+ D**2)/(2*D)
            print ' The maximum curvature is', R
            
            
        #################### The strain of the upper and lower PEDOT layers
            S_up=lengths_up[i][0]/L
            S_down=lengths_down[i][0]/L
            
           # print ' The strain of the upper and  lower PEDOT layers are ', S_up, S_down
            
        
           
            ####################### PEDOT Inertia 
            I= (W* th**3)/12
            
            I1=(((2*W*(th3/2)+ th1)**3)/3)- ((2*W*(th3/2)**3)/3)
            I2=(2*W*(th3/2)**3) /3

            E= ((E1*I1)+ (E2*I2))/ I
            
            ############################## Blocked Force
            s= (E*I)/( R*E1*W*th1*(th1+th2))
            FP=(E2*W*s* th1*(th1+th3))/ L_up
           # print ' E2 is', E2
           # print ' E1 is', E1
          #  print ' The blocked force is', FP
            
            

            
            
            
           ##################### Voltage Signal Trapezoidal Integration
            f= lambda x:sin(x)
            a=0
            b=pi/2
            n=5
            h=(b-a)/n 
            S=0.5*(f(a)+ f(b))
            for i in range(1,n):
                S+= f(a+i*h)
                #print S
            #error    
            Integral = h*S
            
            
          ##################### Energy of Voltage signal
            f= lambda x:sin(x)**2 ##### for actual divide by impedance 
            a=0
            b=pi/2
            n=5
            h=(b-a)/n 
            E_x=0.5*(f(a)+ f(b))
            for i in range(1,n):
                E_x= f(a+i*h)
                #print  E_x
            #error    
            Integral = h* E_x
    
    ################# Equation19, equation 11,12
    
    

    
    
    
    
    
          ############################## #Density of Transfered Charges
            P= W*th*L
            #I(t)=cos(t)
            f= lambda x:sin(x)/P
            a=0
            b=pi/2
            n=5
            h=(b-a)/n 
            Q=0.5*(f(a)+ f(b))
            for i in range(1,n):
                Q+= f(a+i*h)
                #print Q
            #error    
            Integral = h*Q
    

        
        

         
         
           ######################### #Strain of the second PEDOT layer
           # F(t)= sin(t)
            
            f= lambda t:sin(t)/(E2*W*th3) #  F is the force generated by ions
            a=0
            b=pi/2
            n=5
            h=(b-a)/n 
            s2=0.5*(f(a)+ f(b))  # strain of second PEDOT layer
            for i in range(1,n):
                s2+= f(a+i*h)
                #print s2
            #error    
            Integral = s2*h


            
            
        if (self.totalTime >=10 and self.notYetDone): #right arrow => increase mainNode
            self.notYetDone=False
   # def onEndAnimationStep(self,dt):
   
            return 0
    
        


