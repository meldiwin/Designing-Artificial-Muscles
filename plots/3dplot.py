from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = plt.axes(projection='3d')


ax = plt.axes(projection='3d')



data = np.loadtxt('Cl_distance_matrix_1_6.txt',delimiter=',',unpack=True)

x=data[0,:]
y=data[1,:]
z=data[2,:]
#ax.plot3D(x, y, z, 'gray')

ax.scatter3D(x, y, z, c=z, cmap='Greens');

plt.show()
