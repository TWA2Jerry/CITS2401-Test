'''def population(n,r,t,h):
    return n*r**(t/h)

import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
x_pts = np.linspace(0,2*np.pi,10)
y_pts = np.tan(x_pts)
splines = interpolate.splrep(x_pts, y_pts)
x_vals = np.linspace(0,2*np.pi,50)
y_vals = interpolate.splev(x_vals, splines)
plt.plot(x_pts, y_pts, 'o')
plt.plot(x_vals,y_vals, '-x')
plt.show()'''

from mpl_toolkits.mplot3d import Axes3D
import math
import matplotlib.pyplot as plt
import numpy as np

def spiral(a, b, h, n):
    x_array = []
    y_array = []
    z_array = []
    
    for i in range(2*n*20):
         # initialization 
         t = i*(math.pi/20)
         
         #Determine current R value
         #add the generated x point to an array
         #add the generated y point to an array
         #add the generated z point to an array
         r = (a*b*math.exp(-0.04*t))/(math.sqrt((b*(math.cos(t)))**2+(a*math.sin(t))**2))
         x = r*math.cos(t)
         y = r*math.sin(t)
         z = (h*t)/(2*math.pi*n)
         
         x_array.append(x)
         y_array.append(y)
         z_array.append(z)
     
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.plot(x_array,y_array,z_array, label='Elliptical Spiral')
    ax.legend()
    plt.show()
