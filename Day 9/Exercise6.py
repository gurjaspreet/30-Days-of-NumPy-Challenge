import numpy as np


arr = np.array([2, 0, 1, 3, 5])

encoded_arr = np.zeros((arr.size, arr.max() + 1), dtype='int8')
for i in range (len(arr)):
    encoded_arr[i, arr[i]] = 1

print(encoded_arr) 