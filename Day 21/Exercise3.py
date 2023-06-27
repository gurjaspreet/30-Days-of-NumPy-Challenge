import numpy as np


arr = np.array([[3, 2, 1, np.nan], [5, np.nan, 1, 6]])

result = np.isnan(arr)
print(result)