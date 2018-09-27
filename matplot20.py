import numpy as np
import matplotlib.pyplot as plt
p =np.random.standard_normal((50,2))
p += np.array((-1,1)) # center the distribution at (-1,1)

q =np.random.standard_normal((50,2))
q += np.array((1,1)) #center the distribution at (-1,1)


#plt.scatter(p[:,0], p[:,1], color ='m')
#plt.scatter(q[:,0], q[:,1], color = 'c')
#plt.show()
''' Plotting bars'''
vals = np.random.random_integers(99, size =50)
color_set = ['b', 'c', 'm','r']
color_lists = [color_set[(len(color_set)* val) // 100] for val in vals]
#c = plt.bar(np.arange(50), vals, color = color_lists)
#plt.show()
''' Plotting pie charts'''
hi =np.random.random_integers(8, size =10)
color_set =['b', 'c', 'm','r']
##plt.pie(hi, colors = color_set)# colors attribute accepts a range of values
##plt.show()
''' Plotting box'''
values = np.random.randn(100)
##w = plt.boxplot(values)
##for att, lines in w.items():
##    for l in lines:
##        l.set_color('c')
##plt.show()
''' Color Maps'''
import matplotlib.cm as cm
N = 256
angle = np.linspace(0, 8 * 2 * np.pi, N)
radius = np.linspace(.5, 1., N)
X = radius * np.cos(angle)
Y = radius * np.sin(angle)
##plt.scatter(X,Y, c=angle, cmap = cm.hsv)
##plt.show()
''' Line Plots'''
def pq(I, mu, sigma):
    a = 1. / (sigma * np.sqrt(2. * np.pi))
    b = -1. / (2. * sigma ** 2)
    return a * np.exp(b * (I - mu) ** 2)

I =np.linspace(-6,6, 1024)
##
##plt.plot(I, pq(I, 0., 1.), color = 'k', linestyle ='solid')
##plt.plot(I, pq(I, 0., .5), color = 'c', linestyle ='dashed')
##plt.plot(I, pq(I, 0., .25), color = 'r', linestyle ='dashdot')
##plt.show()



def gf(X, mu, sigma):
    a = 1. / (sigma * np.sqrt(2. * np.pi))
    b = -1. / (2. * sigma ** 2)
    return a * np.exp(b * (X - mu) ** 2)

X = np.linspace(-6, 6, 1024)
for i in range(64):
    samples = np.random.standard_normal(50)
    mu,sigma = np.mean(samples), np.std(samples)
##    plt.plot(X, gf(X, mu, sigma), color = '.75', linewidth = .5)

##plt.plot(X, gf(X, 0., 1.), color ='.00', linewidth = 3.)
##plt.show()

N = 15
A = np.random.random(N)
B= np.random.random(N)
X = np.arange(N)
##plt.bar(X, A, color ='w', hatch ='x')
##plt.bar(X, A+B,bottom =A, color ='r', hatch ='/')
##plt.show()
print('#@*@#'*9)

X= np.linspace(-6,6,1024)
Ya =np.sinc(X)

Yb = np.sinc(X) +1
##plt.plot(X, Ya, marker ='o', color ='.75')
##plt.plot(X, Yb, marker ='^', color='.00', markevery= 32)# this one marks every 32 nd element
##plt.show()

import matplotlib as mpl
mpl.rc('lines', linewidth =3)
mpl.rc('xtick', color ='w') # color of x axis numbers
mpl.rc('ytick', color = 'w') # color of y axis numbers
mpl.rc('axes', facecolor ='g', edgecolor ='y') # color of axes 
mpl.rc('figure', facecolor ='.00',edgecolor ='w') # color of figure
mpl.rc('axes', color_cycle = ('y','r')) # color of plots
x = np.linspace(0, 7, 1024)
plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))
plt.show()


