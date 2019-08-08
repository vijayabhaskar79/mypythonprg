import math

#x = [1:10:2]
#print(x)

import matplotlib.pyplot as plt
from pylab import *
import numpy as np

t = np.arange(10,70,10)
u = np.sin(t**np.pi)+sqrt(t)
plt.plot(t,u)
plt.show()
print(t)
print(u)