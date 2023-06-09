import numpy as np

temp = np.zeros((4, 11))
arr = np.linspace(0, 1, 11)
arr = np.vstack((arr, temp))

print(arr)