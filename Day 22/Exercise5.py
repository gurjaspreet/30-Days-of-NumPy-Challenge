import numpy as np


arr = np.zeros((10, 4), dtype='int')

for idx, value in np.ndenumerate(arr):
    if (idx[0] + idx[1]) % 3 == 0:
        arr[idx] = 1

print(arr)