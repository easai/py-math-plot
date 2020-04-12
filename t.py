import matplotlib.pyplot as plt
import math
import numpy as np
from scipy import stats

x=np.arange(-4,4,.1)
l=[]

y=[stats.norm.pdf(x=m, loc=0, scale=1) for m in x]
plt.plot(x,y)
l.append("normal")



df=3
y=[stats.t.pdf(x=m, loc=0, scale=1, df=df) for m in x]
plt.plot(x,y)
l.append(f"{df=}")
df=5
y=[stats.t.pdf(x=m, loc=0, scale=1, df=df) for m in x]
plt.plot(x,y)
l.append(f"{df=}")


plt.legend(l)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title('title')
plt.title("t Distribution PDF")
plt.show()
