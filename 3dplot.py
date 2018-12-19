import math
import photo
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d



fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x, y, z = [range(10)],[range(1,100,10)],[range(20,30)]

ax.plot_wireframe(x,y,z, rstride=3, cstride=3)

plt.show()
