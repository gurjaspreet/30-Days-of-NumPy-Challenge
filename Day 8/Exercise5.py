import numpy as np


arr = np.array(
    [
        [2, 0, 0, 0, 2, 0, 1, 1, 4, 2],
        [3, 2, 0, 4, 4, 0, 1, 1, 2, 1],
        [1, 4, 3, 0, 3, 4, 2, 3, 4, 2],
        [4, 2, 0, 2, 4, 3, 1, 2, 4, 1],
    ]
)

arr = np.delete(arr, 1, axis=0)
arr = np.delete(arr, -1, axis=1)

print(arr)