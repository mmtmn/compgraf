import matplotlib.pyplot as plt

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
plt.show()


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