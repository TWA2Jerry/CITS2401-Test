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

data = np.array([-0.2,1.0,3.5,-3,2])
data[np.where(data < 0)]*=-1
print(data)

myType = [('name','U20'),('height',int),('age',int)]
values = [('Billy',178,18),('Beatrice',182,19),('Bob',160,17)]
students = np.array(values,dtype=myType)

print(np.sort(students,order = 'height'))


data = np.array([(u'Ford', 1.8, u'blue'),(u'Holden', 2.0, u'silver'),(u'Hyundai', 1.6, u'blue')],
dtype=[('make','U10'),('capacity',float),('colour','U10')])

print(data[np.where(data[np.where(data['colour']=='blue')]['capacity']>1.6)])

#print(data[np.where(data['colour']=='blue' and data['capacity']>=1.6)]) Doesn't work because we need either a.any or a.all

# print(data[np.where(data[colour==blue] and data[capacity>1.6])]) doesn't work because colour isn't defined

# print(data[np.where(data['colour']=='blue')] and data[np.where(data['capacity']>1.6)])
# data[np.where(data[colour==blue] and data[capacity>1.6])]
# print(data[np.where(data['colour']=='blue' and data['capacity']>=1.6)])'''

def position(theta1,theta2,l1,l2):
    vert = math.sin(theta1)*l1+math.sin(theta2+theta1)*l2
    hor = math.cos(theta1)*l1+math.cos(theta2+theta1)*l2
    print(hor,vert)
    
def polygon(offset):
    offset = math.radians(offset)
    angles = np.arange(0,2*math.pi,math.pi/3)
    sines = np.sin(angles+offset)
    cosines = np.cos(angles+offset)
    print(cosines,sines)
    plt.plot(cosines,sines)
    plt.show()
    
a = np.array([[1,2,3],
             [4,5,6]])
a = a+1
print(a)

