from __future__ import division
import numpy as np
from sympy import Symbol
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
from numpy import linspace,cos,pi,ceil,floor,arange
import scipy
from scipy import signal, misc
from scipy.integrate.quadpack import quad
from scipy import integrate
from sympy import integrate, Symbol, exp
from sympy.abc import x
from scipy.integrate import quad
import pylab as pl
import sympy as sp
from scipy import integrate
from scipy.integrate.quadpack import quad
from sympy.polys.polyfuncs  import interpolate
import scipy.interpolate
from scipy.interpolate import interp1d
#import serial
import csv
import matplotlib.pyplot as plt
import pandas as pd
import warnings
import matplotlib.cbook
warnings.filterwarnings("ignore",category=matplotlib.cbook.mplDeprecation)




plt.style.use("ggplot")

# Setup


portPath = "/dev/ttyACM0"       # Must match value shown on Arduino IDE
baud = 9600                    # Must match Arduino baud rate
timeout = 5                       # Seconds
filename = "data.csv"
max_num_readings = 16000
num_signals = 1


#def read_serial_data(serial):
    #"""
    #Given a pyserial object (serial). Outputs a list of lines read in
    #from the serial port
    #"""
    #serial.flushInput()
    
    #serial_data = []
    #readings_left = True
    #timeout_reached = False
    
    #while readings_left and not timeout_reached:
        #serial_line = serial.readline()
        #if serial_line == '':
            #timeout_reached = True
        #else:
            #serial_data.append(serial_line)
            #if len(serial_data) == max_num_readings:
                #readings_left = False
        
#return serial_data

#T = 10
#armonics = 10


T = float(input("Enter the periodic time: "))


armonics = float(input("Enter the number of the harmonics: "))


# Fourier Series function
def fourierSeries(n_max,freq,amp,T_f):
    
    def bn(n):
        n = int(n)
        if (n%2 != 0):
            return amp/(np.pi*n)
        else:
            return 0
    
    
    def wn(n):
        global T
        wn = (freq*np.pi*n)/T
        return wn
    
    a0 = 0
    partialSums = a0
    n_max=int(n_max)
    for n in range(1,n_max):
        try:
            #partialSums = partialSums + (amp/(np.pi*n))*np.sin(((freq*np.pi*n)/T)*x)
            
            partialSums = partialSums + bn(n)*np.sin(wn(n)*T_f)
            
        except:
            print("pass")
            pass
    return partialSums



### periodic time 


time_period=T;
final_time=2*time_period;

### total time


T_f = np.linspace(0,final_time,1000, endpoint=True)

n_max= armonics

T_f_=np.linspace(0,final_time,1000, endpoint=True)


#### signal#####



max_val_T = float(input("Enter the final value of the measured time in seconds: "))

T_f= np.linspace(0,max_val_T,10000)
n_max= armonics
axis_color = 'lightgoldenrodyellow'
fig = plt.figure()
ax = fig.add_subplot(111)

# Adjust the subplots region to leave some space for the sliders and buttons
fig.subplots_adjust(left=0.25, bottom=0.25)


amp_0 = 0
freq_0 = 0



   
[line] = ax.plot(T_f, fourierSeries(n_max, freq_0, amp_0,T_f), linewidth=2, color='red')

max_v_limit = float(input("Enter the maximum value of the voltage positive axis: "))
mini_v_limit = float(input("Enter the minimum value of the voltage positive axis: "))

ax.set_xlim([0, max_val_T ])
ax.set_ylim([mini_v_limit, max_v_limit])




# Define an axes area and draw a slider in it
amp_slider_ax = fig.add_axes([0.25, 0.15, 0.65, 0.03], axisbg=axis_color)


amp_slider = Slider(amp_slider_ax, 'Amp', 0.01, 10, valinit=amp_0)

# Draw another slider
freq_slider_ax = fig.add_axes([0.25, 0.1, 0.65, 0.03], axisbg=axis_color)
freq_slider = Slider(freq_slider_ax, 'Freq', 0.01, 20, valinit=freq_0)


# Define an action for modifying the line when any slider's value changes
def sliders_on_changed(val):
    #print "Amplitude: ",  amp_slider.val
    #print "Frequency: ",  freq_slider.val
    line.set_ydata(fourierSeries(n_max, freq_slider.val,amp_slider.val, T_f))
    fig.canvas.draw_idle()
amp_slider.on_changed(sliders_on_changed)
freq_slider.on_changed(sliders_on_changed)





# Add a button for resetting the parameters
reset_button_ax = fig.add_axes([0.8, 0.025, 0.1, 0.04])
reset_button = Button(reset_button_ax, 'Reset', color=axis_color, hovercolor='0.975')

def reset_button_on_clicked(mouse_event):
    f= open("final signal",'w')
    print ("Amplitude Gain: ",  amp_slider.val)
    print ("Frequency Gain: ",  freq_slider.val)
    
    
    ####### signal  
    signal_raw=[]
    for i in T_f:
        signal_raw.append(fourierSeries(armonics,i,amp_slider.val, freq_slider.val))
     
    f.write( str(signal_raw) + "\n")
    final_signal= np.array(signal_raw)
    
    #print "final_signal", final_signal
   
    
    
    wn = (freq_slider.val*np.pi)/T
    
    print ('actual frequency is', wn)
    actual_amp= amp_slider.val/(np.pi)
    print ('actual amp is', actual_amp)
    #print final_signal$$
    freq_slider.reset()
    amp_slider.reset()
    

 

    
    
    
    ### writing signal
    
    
    L=0.01 # the length of the actuator
    N=10# number of spatial samples


    u0=0   # s

    u0s=0### the voltage before the clamping at t is zero
#### the final value that voltage will reach at the space


    '''  https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2871148/'''

######  getting actual values of C 







    c=0.002
    
    R=12e6
    t_elapsed= 0.0001
    Ke=9e9
    A=2.167e-6
    th_sq=6.25e-10

    dx=L/N  ### space step
    
    
    alpha=0.0002# the inverse of tau (real value)
#0.0002# time step
    t_final= max_val_T ### two minutes 
    dt= 0.0001
    b=2.167e-3
    h= 2.5e-5

    Inertia= (b*h**3)/12

#### flexure rigidity
    Young_Modulus= (12*4.1*(0.0063)**3)/(3*2.167e-3*(2.5e-5)**3)




    x=np.linspace(dx, L, N)  ### space


    u=np.zeros(N)*u0
    dudt=np.empty(N)  ### empty vector


    
    ##### fixing error 
    '''sampling '''
    Fsampling=1000;
    ts=1/Fsampling
    txs=np.arange(0,(final_time+ (ts/2)), ts)
    r=len(T_f)/len(txs)
    xts=np.arange(0,len(T_f),r).astype('int')
    xs=T_f[xts]
    ys=final_signal[xts]

    
    
    #fig1=plt.figure()
    #plt.plot(xs,u,color='blue', linestyle=' ', marker='o')
    #plt.bar(xs,u, bottom=0, width=0.3, color='blue')
    #plt.axhline(0,color='black', linestyle='-', linewidth=0.2)
    
    #fig2 = plt.figure()
    #plt.plot(xs,u)
    #plt.show()


    
    #
    #i=0;
    #for i in np.arange(0,len(u)-1):
        #i=i+1
        #i=i
        #u[i]
        
 ############################ initial U[0]       
    u[0]=0;
    f= open("Force Diffusion Values.txt",'w')
    f2= open("volt Diffusion Values.txt",'w')
    for q in range(0,len(ys)-1):
        q=q+1
        q=q;
        u[0]=ys[q]## sampling rate
        u[0]=u[0]
        
        #print u[q]
        #f.write( str(u[0]) + "\n"  )
       
        #t= np.arange(0,max_val_T ,dt)# iteration
        for j in range(0,len(u)):
            for i in range(1,N-1):  
                dudt[i]= alpha*(-(u[i]-u[i-1])/dx**2+(u[i+1]-u[i])/dx**2) 
        u=u+dudt*dt
        u[N-1] = u[N-2];
        #print u
        #f.write( str(u) + "\n"  )
        
        '''check the electronic and ionic charge ''' 
    
        q= c*u*(1-np.exp(-t_elapsed*alpha))
        
    #print q
  
  
        stress= (Ke*q**2)/(A* th_sq)
    
        bending_stress=  (Ke*q**2 * np.sin(89.9))/(A* th_sq) 
    
                    #### axial force
        Force= stress*A*1e6
        
     
        
        
        ### Hystersis  modeling nonlinearities
        
        
        ## stress relaxation
        
        
        
        
        #f.write( str(Force[9]) + "\n"  )




        Moment_neutral= (Inertia*bending_stress)/h
    ### moment curvature
        Curvature= Moment_neutral/(Young_Modulus* Inertia)
    
        
        ### RMS
        
        
        
        ### effect of temperature/ relaxation time
   
         
        ### Condition of ion concentration( saturation) time of flight ( using my previous model)
  


reset_button.on_clicked(reset_button_on_clicked)





plt.grid(True)
plt.show()
