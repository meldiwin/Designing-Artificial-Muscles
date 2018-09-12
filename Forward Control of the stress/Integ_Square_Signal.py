from __future__ import division
import  matplotlib.pyplot as plt
from scipy.interpolate import interp1d
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
import numpy as np
from scipy.interpolate import interp1d



T = 40
 ### harmonics
n=4


def bn(n):
    n = int(n)
    if (n%2 != 0):
        return 4/(sp.pi*n)

    else:
        return 0
        
        
def wn(n):
    global T
    wn = (2*sp.pi*n)/T
    return wn
    
    
 

T_f=sp.Symbol('T_f')


partialSums = 0
for n in range(1,100):  #armonics
    partialSums = partialSums+ bn(n)*sp.sin(wn(n)*T_f)
  
   
## integration 
f= open("Sampled Integrated Signal",'w')

### integrated signal
integ=sp.integrate(partialSums,T_f)
for  q in range(1,101,1): 
    signal_integ=integ.subs({T_f:(q)})
    #final_signal=np.array(signal_integ)
    
    f.write( str(signal_integ) + "\n")
    




    
##### sampling
#T_final = np.linspace(0,100,1000, endpoint=True)

#Fsampling=1000;
#ts=1/Fsampling
#txs=np.arange(0,(100+ (ts/2)), ts)
#r=len(T_final)/len(txs)
#xts=np.arange(0,len(T_final),r).astype('int')
##xs=T_final[xts]
#ys=final_signal[xts]

#


    
    ##### sampling
    


    
    
   
    
    