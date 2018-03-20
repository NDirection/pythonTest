
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


fig = plt.figure()
ax =Axes3D(fig)

#X Y value
X = np.arange(-4,4,0.25)

print(X)
Y = np.arange(-4,4,0.25)


X,Y = np.meshgrid(X,Y)

print(X)

print("#######")


print(Y)
R = np.sqrt(X**2 + Y**2)

#high value
Z=np.sin(R)

ax.plot_surface(X,Y,Z , rstride= 1 ,cstride= 1 ,cmap = plt.get_cmap("rainbow"))

ax.contourf(X,Y,Z,zdir='x',offset= -4 ,cmap =plt.get_cmap('terrain'))

plt.show()