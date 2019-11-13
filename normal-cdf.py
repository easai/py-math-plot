import matplotlib.pyplot as plt
import math
import numpy as np
from scipy import stats

x=np.arange(-4,4,.01)
l=[]

for i in np.linspace(.5,3,5):
    y=[stats.norm.cdf(x=m, loc=0, scale=i) for m in x]
    plt.plot(x,y)
    l.append("n = "+str(i))

plt.legend(l)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title('title')
plt.title("Normal Distribution PDF")
plt.show()
