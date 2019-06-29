import matplotlib.pyplot as plt
import math
import numpy as np

a=np.arange(0,4,.01)
x= np.linspace(0,10,100)
l=[]
for i in range(1,5):
    y= i*np.exp(-i*a)
    plt.plot(a,y)
    l.append("n = "+str(i))

plt.legend(l)
plt.xlabel("x")
plt.ylabel("f(x)=n*e^(-n*x)")
igfont = {'family':'Meirio'}
plt.title('title',**igfont)
plt.title("Exponential Distribution PDF")
plt.show()
