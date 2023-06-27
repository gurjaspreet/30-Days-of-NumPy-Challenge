import numpy as np


arr = np.array([4, 3, 5, np.nan, 5, 3, np.nan], dtype='float')

arr[np.isnan(arr)] = 0
print(arr)