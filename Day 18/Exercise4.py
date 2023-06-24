import numpy as np


arr = np.array(
    [
        [4, 3, 6],
        [5, 2, 7],
        [8, 3, 10],
        [-3, 4, 2],
    ]
)

arr_sorted = np.apply_along_axis(np.sort, axis=1, arr=arr)
print(arr_sorted)