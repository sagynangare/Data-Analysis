import numpy as np
import matplotlib.pyplot as plt
import threading
def plot_curve():
    X = np.linspace(0, 2 * np.pi, 50, endpoint=True)
    F = np.sin(X)
    plt.plot(X,F)
    startx, endx = -0.1, 2*np.pi + 0.1
    starty, endy = -1.1, 1.1
    plt.axis([startx, endx, starty, endy])
    plt.show()

    
def plot_mix():
    X = np.linspace(-2 * np.pi, 2 * np.pi, 50, endpoint=True)
    F1 = 3 * np.sin(X)
    F2 = np.sin(2*X)
    F3 = 0.3 * np.sin(X)
    startx, endx = -2 * np.pi - 0.1, 2*np.pi + 0.1
    starty, endy = -3.1, 3.1
    plt.axis([startx, endx, starty, endy])
    plt.plot(X,F1)
    plt.plot(X,F2)
    plt.plot(X,F3)
    plt.show()
t1=threading.Thread(target=plot_curve)
t2=threading.Thread(target=plot_mix)

t1.start()
t1.join()
t2.start()
t2.join()
