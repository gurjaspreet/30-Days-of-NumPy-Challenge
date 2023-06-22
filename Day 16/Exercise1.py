import numpy as np


arr1 = np.arange(12).reshape(-1, 4)
arr2 = np.array([[4, 3, 7, 2], [0, 5, 2, 6]])

arr = np.append(arr1, arr2, axis=0)
print(arr)