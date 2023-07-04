import numpy as np

arr = np.arange(50).reshape((10, 5))
arr = np.char.zfill(arr.astype('str'), 2)
print(arr)