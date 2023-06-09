import numpy as np

x = np.linspace(0, 1, 11)
y = np.linspace(0, 1, 11)

xx, yy = np.meshgrid(x, y)

print(xx)
print(yy)