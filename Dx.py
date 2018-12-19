from IPython.display import display
import math
import photo
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
#import matplotlib.use('Qt4Agg')
from mpl_toolkits.mplot3d import axes3d
from matplotlib import animation
#plt.rcParams['animation.ffmpeg_path'] = '~/ffmpeg'

visualSpectrum = np.arange(390, 710, 20)
frange = np.arange(1, 16)

##Dx = []
##for wvlnth in visualSpectrum:
##    d = photo.Dx(16, wvlnth)
##    Dx.append(round(d,2))
##
##print(Dx)
##
##print('\n', photo.Dx(1.8, 390),photo.Dx(1.8, 700))
##
##plt.plot(Dx, visualSpectrum, c='green', ls=':')
##
##Dx = []
##for f in frange:
##    for wvlnth in visualSpectrum:
##        d = photo.Dx(f, wvlnth)
##        Dx.append(round(d,2)
##
##print(Dx)
##
##print('\n', photo.Dx(1.8, 390),photo.Dx(1.8, 700))
##
##plt.plot(Dx, visualSpectrum, c='green', ls=':')

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = frange
y = visualSpectrum
x, y = np.meshgrid(x, y)
zs = np.array([photo.Dx(x,y) for x,y in zip(np.ravel(x), np.ravel(y))])
z = zs.reshape(x.shape)

print(zs)
print(len(zs))

color = [str(item/255.) for item in y]

ax.scatter(x, y, z, s=6, c=x, cmap='hot', marker='o')

ax.mouse_init()

ax.set_xlabel('aperature')
ax.set_ylabel('wavelength')
ax.set_zlabel('Dx')

#ax.view_init(30, 90)
#plt.draw()
#plt.show()

display(plt.show())

#anim = animation.FuncAnimation(fig, animate, init_func=init, frames=360, interval=20, blit=True)
#anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

#plt.show()

##Axes3D.plot_surface(visualSpectrum, Dx. frange)
##
##plt.plot_surface.show()
