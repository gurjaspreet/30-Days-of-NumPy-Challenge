import numpy as np

arr = np.zeros((6, 6), dtype='int')
arr[::2, ::2] = 2
arr[1::2, ::2] = 4
print(arr)