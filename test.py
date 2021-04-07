# to run this project: main.py
# made by Thiago M Nóbrega

import math as m
import matplotlib.pyplot as plt

# parametric equation 
# x = 2 cos t
# y = sin t

i = 0.0
r = int(input("Size of the radius of the circle: (please use int values)"))
x = []
y = []
lines = int(input("how many lines? "))
while i < lines+1:
    cos = m.cos(i)
    sin = m.sin(i)
    rcos = 2*r*cos
    rsin = r*sin
    x.append(rcos)
    y.append(rsin)
    del rcos, rsin
    i = i + 1

plt.scatter(x,y)
plt.plot(x, y)
plt.show()





"""import matplotlib.pyplot as plt

x = []
y = []

x.append(12)
x.append(2)
x.append(3)

y.append(1)
y.append(2)
y.append(3)

plt.scatter(x,y)
plt.plot(x, y)
plt.show()"""


"""import matplotlib.pyplot as plt
import matplotlib.lines as mlines

def newline(p1, p2):
    ax = plt.gca()
    xmin, xmax = ax.get_xbound()

    if(p2[0] == p1[0]):
        xmin = xmax = p1[0]
        ymin, ymax = ax.get_ybound()
    else:
        ymax = p1[1]+(p2[1]-p1[1])/(p2[0]-p1[0])*(xmax-p1[0])
        ymin = p1[1]+(p2[1]-p1[1])/(p2[0]-p1[0])*(xmin-p1[0])

    l = mlines.Line2D([xmin,xmax], [ymin,ymax])
    ax.add_line(l)
    return l

import numpy as np
x = np.linspace(0,10)
y = x**2

p1 = [1,1]
p2 = [6,70]

plt.plot(x, y)
newline(p1,p2)
plt.show()"""