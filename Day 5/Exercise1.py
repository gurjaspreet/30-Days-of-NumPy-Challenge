import numpy as np


arr = np.array([[4, 2, 1], [6, 4, 2]])

arr = np.expand_dims(arr, axis=0)

print(arr)