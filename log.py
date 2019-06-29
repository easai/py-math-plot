import matplotlib.pyplot as plt
import math
import numpy as np

x= np.linspace(.1,10,100)
y= [math.log(i) for i in x]
plt.plot(x,y)
plt.show()
