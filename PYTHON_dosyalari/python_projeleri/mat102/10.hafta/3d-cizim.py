import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm 

f = lambda x, y: (4*x**2+y**2)*np.exp(-x**2-y**2)
x = np.linspace(-3, 3, 50)
y = np.linspace(-3, 3, 50)
X, Y = np.meshgrid(x,y)
F = f(x,y)

fig = plt.figure(figsize = [15,15])
ax = fig.gca (projection = '3d')
ax.plot_surface(X, Y ,F, cmap=cm.coolwarm)