import numpy as np

arr = np.zeros((9, 9), dtype=int)

for (i, j), value in np.ndenumerate(arr):
    arr[i, j] = i ** 2 + j ** 2

arr = np.sqrt(arr)

for (i, j), val in np.ndenumerate(arr):
    arr[i, j] = int(val) == val

print(arr.astype(int))