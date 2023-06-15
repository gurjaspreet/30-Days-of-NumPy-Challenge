import numpy as np


np.random.seed(42)
arr = np.random.randn(8, 4)

arr = np.delete(arr, [2], axis = 1)

print(arr)