import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

#x= np.linspace(0.64,.67,4)
x= np.linspace(0.9,1.1,10)

for i in x:
#    y=norm.cdf(i)*.5+norm.cdf(2-i)
    y=norm.cdf(i)+norm.cdf(2-i)
#    z=1/3*(1-norm.cdf(i))+2/3*(1-norm.cdf(2-i))
#    print(f"{i}: {y}: {z}")
    print(f"{i}: {y}")
    


