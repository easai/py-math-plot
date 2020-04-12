import matplotlib.pyplot as plt
import math
import numpy as np
from scipy import stats

l=[]
x = np.arange(0, 1, .01)  # global
x = np.arange(0.001, 1, .001)
y0 = [stats.norm.ppf(m, loc=0, scale=1) for m in x]
plt.plot(y0, y0)
l.append("n=1")

def theoretical_empirical():
    x=[.01,.1,.2,.28,.8]
    y0 = [m for m in x]
    plt.plot(y0,y0)
    l.append("n=1")

def F(t,x):
    sum = 0
    for val in x:
        if x>t:
            sum+=1
    return sum/len(x)

def uniform_test():
    x=[.28,.2,.01,.8,.1]
    n=len(x)
    for i,val in enumerate(x):
        plt.scatter((i+1)/n, val)
        print(f"{(i+1)/n=} {val=}")
    unif=[m for m in x]
    plt.plot(x,unif)
    l.append('Unif')


def uniform():
    unif=[m for m in x]
    plt.plot(y0,unif)
    l.append('Unif')


def uniform_shift():
    unif=[2*math.sqrt(3)*m-math.sqrt(3) for m in x]
    plt.plot(y0,unif)
    l.append('Unif shift')

# uniform_shift()

def exponential(a):
    exp=[-1/a*math.log(1-m) for m in x] # Note it's inverse func of CDF 1-exp(-x)
    plt.plot(y0,exp)
    l.append(f'Exp {a=}')

# exponential(1)
# exponential(2.5)

def cauchy():
    exp=[math.sqrt(1/(math.pi*m)-1) if 1/(math.pi*m)-1 > 0 else 0 for m in x]
    plt.plot(y0,exp)
    l.append('Cauchy')
    exp=[-math.sqrt(1/(math.pi*m)-1) if 1/(math.pi*m)-1 > 0 else 0 for m in x]
    plt.plot(y0,exp)
    l.append('Cauchy')

# cauchy()

def laplace(a):
    exp=[-1/math.sqrt(a)*(math.log(m*2/a)) for m in x]
    plt.plot(y0,exp)
    l.append('Laplace')
    exp=[1/math.sqrt(a)*(math.log(m*2/a)) for m in x]
    plt.plot(y0,exp)
    l.append('Laplace')

# TODO merge branches
# laplace(math.sqrt(2))

def lightrighttail():
    n = 1.5
    yright=[stats.norm.ppf(m, loc=0, scale=n) for m in x]
    plt.plot(y0,yright)
    l.append(f"{n=} right thinner")

lightrighttail()

def lightlefttail():
    n=.5
    yleft=[stats.norm.ppf(m, loc=0, scale=n) for m in x]
    plt.plot(y0,yleft)
    l.append("n=.5 left thinner")

lightlefttail()

plt.legend(l)
# plt.xlim(-30,30)
# plt.ylim(-30,30)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title('title')
plt.title("Normal Distribution PDF")
plt.show()
