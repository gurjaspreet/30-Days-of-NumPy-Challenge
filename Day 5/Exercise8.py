import numpy as np


arr = np.full((10, 4), fill_value=False)

arr = arr.reshape((5, 2, 4))

print(arr)