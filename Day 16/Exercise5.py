import numpy as np


arr = np.array(
    [
        [0, 1, 5, 7],
        [8, 9, 2, 5],
    ]
)
arr = np.row_stack((arr, np.array([3, 4, 6, 7], dtype='int')))
print(arr)