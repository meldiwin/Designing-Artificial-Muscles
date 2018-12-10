import sys
import numpy as np
import matplotlib.pyplot as plt
import warnings
import matplotlib.cbook
warnings.filterwarnings("ignore",category=matplotlib.cbook.mplDeprecation)
import matplotlib.font_manager as font_manager
from mpl_toolkits.mplot3d import Axes3D




fig = plt.figure()



data_1 = np.loadtxt('Cl_distance_matrix_1_6.txt',delimiter=',',unpack=True)
data_2 = np.loadtxt('Cl_scan_distance_1_6.txt',delimiter=',',unpack=True)
data_3 = np.loadtxt('Cl_without_distance_1_6.txt',delimiter=',',unpack=True)

o_1=data_1[0,:]
x_1=data_1[1,:]
o_2=data_2[0,:]
x_2=data_2[1,:]
o_3=data_3[0,:]
x_3=data_3[1,:]

plt.plot(o_1, x_1,'*',  linewidth=1, label='Cl') # avoid markers by spec. line type
plt.plot(o_2, x_2,'x',  linewidth=1, label= 'Cl_scan') # avoid markers by spec. line type
plt.plot(o_3, x_3,'^',  linewidth=1, label= 'Cl_free') # avoid markers by spec. line type
plt.legend(loc='upper left', prop={"family":"Times New Roman"})
plt.title('Distance_matrix_1_6')
plt.show()






