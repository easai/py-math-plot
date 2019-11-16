import matplotlib.pyplot as plt
import math
import numpy as np
from scipy import stats

x=np.arange(-4,4,.01)
l=[]

# for i in np.linspace(.5,3,5):
for a in range(3,1):
    for b in range(3, 1):
        y=[m**a*(1-x)**b for m in x]
        plt.plot(x,y)
        l.append(f"a= ")



plt.legend(l)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title('title')
plt.title("Normal Distribution PDF")
plt.show()
