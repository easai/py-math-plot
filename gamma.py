import matplotlib.pyplot as plt
import math
import numpy as np
from scipy import stats

x=np.arange(0,4,.01)
l=[]

def gamma(x,a):
    y=stats.gamma(x,a)
    return y

for i in np.linspace(1.5,3,5):
    y=[stats.gamma.pdf(x=m, a=i) for m in x]
    # y=[norm(m,0,i) for m in x]
    plt.plot(x,y)
    l.append("n = "+str(i))

plt.legend(l)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title('title')
plt.title("Gamma Distribution PDF")
plt.show()
