import numpy as np
import random
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import Coordinates

from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
plt.ion()
fig = plt.figure(figsize=(4, 4))

ax = fig.add_subplot(111, projection='3d')
axlist = []
for i in np.arange(20):
    phi = random.uniform(0, 2 * np.pi)
    costheta = random.uniform(-1, 1)
    u = random.uniform(0, 1)

    size = 100
    theta = np.arccos(costheta)
    r = (size / 2) * np.sqrt(u)

    x = r * np.sin(theta) * np.cos(phi)
    y = r * np.sin(theta) * np.sin(phi)
    z = r * np.cos(theta)
    axlist.append(ax.scatter(x, y, z, c="red"))
plt.ion()


plt.show()







mean = [0, 0]
cov = [[100, 100], [100, 0]]
for i in np.arange(100):
    x, y = np.random.multivariate_normal(mean, cov, 1).T
    plt.plot(x, y, 'x')
plt.axis('equal')
plt.show()
print("test")