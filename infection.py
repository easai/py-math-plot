import matplotlib.pyplot as plt
import math
import numpy as np
from matplotlib.font_manager import FontProperties

fp = FontProperties(fname=r'C:\WINDOWS\Fonts\meiryo.ttc', size=14)
l=[]
a= math.pow(2,1/9.0)
b= math.pow(2,1/5.0)
c= math.pow(2,1/3.0)
x= np.linspace(0,15,100)
ya= [a**i for i in x]
plt.plot(x,ya)
l.append("9日で倍")
yb=[b**i for i in x]
plt.plot(x,yb)
l.append("5日で倍")
yc=[c**i for i in x]
plt.plot(x,yc)
l.append("3日で倍")


plt.legend(l,prop=fp)
plt.show()

