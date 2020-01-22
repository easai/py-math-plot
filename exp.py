import matplotlib.pyplot as plt
import math
import numpy as np

x= np.linspace(0,5,100)
y= [math.exp(i) for i in x]
plt.plot(x,y)
z= [1+i+1/2*i*i+1/6*i**3+1/24*i**4+1/120*i**5+1/720*i**6+1/5040*i**7+1/40320*i**8+1/362880*i**9 for i in x]
plt.plot(x,z)

plt.show()
