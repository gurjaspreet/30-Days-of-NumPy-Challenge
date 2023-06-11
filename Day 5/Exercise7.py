import numpy as np


arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

row = arr[np.newaxis, :]
column = arr[:, np.newaxis]

print(row)
print(column)