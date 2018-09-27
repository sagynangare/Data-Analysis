import matplotlib.pyplot as plt
import numpy as np
from numpy.random import normal,rand
def fun1():
    x = normal(size=200)
    a = np.linspace(0, 10, 100)
    b = np.exp(-a)
    plt.plot(a, b)
    plt.show()
print('#'*9)
print('#'*5+'Histogram'+'#'*5)
def fun2():
    x = normal(size=200)
    plt.hist(x, bins=30)
    plt.show()

print('#'*5+'Scatter plot'+'#'*5)
def fun3():
    a = rand(100)
    b = rand(100)
    plt.scatter(a, b)
    plt.show()
fun1()
fun2()
fun3()
