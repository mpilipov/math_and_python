import math

import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return math.sin(0.2*x)*math.exp(0.1*x)+5*math.exp(-0.5*x)

print(type(f(1)))
print(f(15))

b=[f(1),f(15)]
a=[[1, 1],[1, 15]]
b=np.array([f(1),f(15)])
a=np.array([[1,1],[1,15]])
t=np.linalg.solve(a,b)
print(t)

x=[1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,11.0,12.0,13.0,14.0,15.0]
y=[math.sin(0.2*i)*math.exp(0.1*i)+5*math.exp(-0.5*i) for i in x]
plt.plot(x, y)
x=[1.0, 15.0]
plt.plot(x, t)

b=[f(1),f(8), f(15)]
a=[[1, 1, 1 ],[1, 8, 8],[1, 15, 15]]
b=np.array([f(1.0), f(8.0), f(15.0)])
a=np.array([[1.0, 1.0, 1.0], [1.0, 8.0, 8.0], [1.0, 15.0, 15.0]])
t=np.linalg.solve(a, b)
print(t)
x=[1.0,8.0,15.0]
plt.plot(x, t)
plt.show()
