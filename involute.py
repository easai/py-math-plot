import matplotlib.pyplot as plt
import math
import numpy as np

t= np.linspace(0, 3*math.pi,100)
x =[math.cos(i)+i*math.sin(i) for i in t]
y= [math.sin(i)-i*math.cos(i) for i in t]
plt.plot(x,y)
plt.show()
