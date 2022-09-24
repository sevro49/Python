import numpy as np
import matplotlib.pyplot as plt
plt.axes(projection = 'polar')

rads = np.arange(0, 2*np.pi, 0.001)

r1 = -2*np.cos(rads)
r2 = 1

plt.polar(rads, r1, 'r.')
for rad in rads:
    plt.polar(rad, r2, 'g.')

plt.fill_between(rads, r1, r2, where = [rads > 2*np.pi/3 and rads < 4*np.pi/3 for rad in rads])

plt.show()
