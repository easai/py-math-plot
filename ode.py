import math

import matplotlib.pyplot as plt
import numpy as np

tlist = np.arange(-1.5, 1.5, .1)
l = []

for i in np.arange(-100, 100, 25):
    for j in np.arange(-100, 100, 25):
        x = [-i*math.e ** (-t) + -j*math.e ** (-1.8*t) for t in tlist]
        y = [i*math.e ** (-t) + .1*j*math.e ** (-1.8*t) for t in tlist]
        plt.plot(x, y)
        l.append("c = " + str(i))

#plt.legend(l)
plt.xlabel("x")
plt.ylabel("y")
plt.title('title')
plt.title("ODE lambda=-1,-1.8")
plt.show()
