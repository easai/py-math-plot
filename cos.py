import matplotlib.pyplot as plt
import math
import numpy as np

x= np.linspace(-math.pi,math.pi,100)
y= [math.cos(i) for i in x]
plt.plot(x,y)
plt.show()
