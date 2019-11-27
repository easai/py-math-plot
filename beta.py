import matplotlib.pyplot as plt
import math
import numpy as np
from scipy import stats

x=np.arange(0,1,.01)
l=[]

# for i in np.linspace(.5,3,5):
# for a in range(1,3):
#     for b in range(1,3):
#         # y=[m**(a-1)*(1-x)**(b-1) for m in x]
#         y=[m for m in x]
#         plt.plot(x,y)
#         l.append(f"a= ")

for a in range(3,4):
    for b in range(3, 4):
        aval=a*.5
        bval=b*.3
        y=[(m**(aval-1))*((1-m)**(bval-1)) for m in x]
        plt.plot(x,y)
        l.append(f"{aval=} {bval=}")


plt.legend(l)
plt.xlabel("x")
plt.ylabel("p")
plt.title('title')
plt.title("Beta Distribution PDF")
plt.show()
