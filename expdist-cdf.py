import matplotlib.pyplot as plt
import math
import numpy as np

a=np.arange(0,6,.01)
x= np.linspace(0,10,100)
l=[]
for i in range(1,5):
    z= 1-np.exp(-i*a)
    plt.plot(a,z)
    l.append("n = "+str(i))

plt.legend(tuple(l))
plt.xlabel("x")
plt.ylabel("F(x)=1-e^(-n*x)")
plt.title("Exponential Distribution CDF")
plt.show()
