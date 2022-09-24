
import numpy as np
import matplotlib.pyplot as plt
plt.axes(projection = 'polar')

rads = np.arange(0, 2*np.pi, 0.001)
r1 = 1
r2 = 1 - np.cos(rads)

for rad in rads:
    plt.polar(rad, r1, 'g.')

plt.polar(rad, r2, 'r.')
plt.fill_between(rads, r1, r2, where =[rads < np.pi/2 and rads>0 for rads in rads])
plt.fill_between(rads, r1, r2, where =[rads < 3*np.pi/2 and rads>2*np.pi for rads in rads])

plt.show()