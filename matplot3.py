import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 5, 0.1);
y = np.sin(x)
z=np.cos(x)
plt.plot(y,color='m')
plt.plot(z,color='c')
plt.show()
