import numpy as np
import matplotlib.pyplot as plt
f = lambda x, y: (4*x**2 + y**2)*np.exp(-x**2-y**2)

x = np.linspace(-3, 3, 50)
y = np.linspace(-3, 3, 50)
X, Y = np.meshgrid(x,y)
F = f(x,y)

plt.contour(X,Y,F)
