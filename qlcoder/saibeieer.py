from numpy import *

def F(t):
    return 750*t*(1-t)**2 + 500*t ** 3

def G(t):
    return 100*(1-t)**3  + 900*t**2 * (1-t) + 500*t**3

def cx(t):
    return F(t)

def cy(t):
    return G(t)

N=5000
t=linspace(0,1,N)
dt=1/N
x=cx(t)
y=cy(t)

dx=array(x[1:])-array(x[:-1])
dy=array(y[1:])-array(y[:-1])

print(sum(sqrt(dx**2+dy**2)))