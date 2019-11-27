import matplotlib.pyplot as plt
import math
import numpy as np
from scipy import stats

x=np.arange(-4,4,.01)
l=[]

def norm(x,mean,var):
    y=1/math.sqrt(2*math.pi*var)*math.exp(-(x-mean)**2/(2*var))
    return y

for i in np.linspace(1,3,5):
    # y=[stats.norm.pdf(x=m, loc=0, scale=i) for m in x]
    y=[norm(m,0,i) for m in x]
    plt.plot(x,y)
    l.append("n = "+str(i))

plt.legend(l)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title('title')
plt.title("Normal Distribution PDF")
plt.show()
