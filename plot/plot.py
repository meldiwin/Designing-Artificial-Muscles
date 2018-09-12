import scitools.std as plt
import sys
import numpy as np
import matplotlib.pyplot as plt




x,y = np.loadtxt('volt.txt',delimiter=',',unpack=True)



plt.figure(1)
plt.plot(x, y,'*',  linewidth=1) # avoid markers by spec. line type
#plt.xlim([0.0, 10])
#plt.ylim([0.0, 2])
plt.legend([ 'Force-- Tip' ], loc='upper right', prop={"family":"Times New Roman"})
plt.xlabel('Sampled time');  plt.ylabel( '$Force /m$')
plt.savefig('volt1v.png')
plt.savefig('volt1v.pdf')
plt.hold(True)






