import matplotlib.pyplot as plt
import math
import numpy as np
from scipy import stats

x=np.arange(-4,4,.01)
l=[]

y=[stats.norm.cdf(x=m, loc=0, scale=1) for m in x]
plt.plot(x,y)
l.append("normal")

y=[stats.t.cdf(x=m, loc=0, scale=1, df=3) for m in x]
plt.plot(x,y)
l.append("t")
y=[stats.t.cdf(x=m, loc=0, scale=1, df=5) for m in x]
plt.plot(x,y)
l.append("t")


plt.legend(l)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title('title')
plt.title("Normal Distribution PDF")
plt.show()
