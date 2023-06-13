import numpy as np


arr = np.arange(12, dtype='int').reshape(-1, 4)

arr = arr[::-1, :]

print(arr)