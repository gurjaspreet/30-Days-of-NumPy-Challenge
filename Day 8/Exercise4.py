import numpy as np


arr = np.array([0, 0, 0, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0, 0])

arr = np.trim_zeros(arr)

print(arr)