import numpy as np
import scipy.special as sp
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import ListedColormap


def circular_holes(radii,NoH,D = 0.1,resolution = 1000):

    if len(radii) != len(NoH) :
        print("Length of radii and NoH differ !")
        return np.zeros((resolution,resolution))

    x=np.linspace(-10,10,resolution)
    y = np.linspace(-10,10,resolution)
    [X,Y] = np.meshgrid(x,y)
    r = np.sqrt(X**2+Y**2)
    A = 2*np.pi * D**2 / 4 * sp.j1(np.pi * D * r)/(np.pi * D * r)

    B = np.zeros((resolution,resolution))

    for m in range(len(radii)):
        R = radii[m]
        N = NoH[m]
        phi = np.pi * 2 * np.arange(N)/N
        z = R * np.exp(1j * phi)
        for k in range(N):
            x = np.real(z[k])
            y = np.imag(z[k])
            B = B + np.exp( 2j* np.pi * x * X) * np.exp( 2j * np.pi * y * Y)

    # Ok, normally, it should be the square of the modulus, for the intensity.
    # However, to get a nicer picture that actually corresponds better to
    # what your eye would see, well...
    F = np.sqrt(np.abs(A * B))

    return F

fig_diff = circular_holes([1,2],[12,6])
# Green color map
nmax = 256
values = np.ones((nmax, 4))
values[:, 0] = np.linspace(0, 0, nmax)
values[:, 1] = np.linspace(0, 1, nmax)
values[:, 2] = np.linspace(0, 0, nmax)
newcmp = ListedColormap(values)

#plt.imshow(fig_diff,cmap = newcmp)
plt.imsave('PyDiffigure.png',fig_diff,cmap = "cool")
plt.show()
