import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, (3*np.pi), 1000)
x = np.sin(np.pi * t/2)
y = t

plt.axvline()
plt.axhline()
plt.plot(x,y)
plt.show()