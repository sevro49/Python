import numpy as np
import matplotlib.pyplot as plt
plt.axes(projection = 'polar')
rads = np.arange(0, (2*np.pi), 0.01)
for rad in rads:
    r = 1-np.cos(rad)
    plt.polar(rad, r, 'r.')

plt.show()