import numpy as np


arr = np.array(
    [
        [0, 1],
        [2, 3],
        [4, 5],
        [6, 7],
        [8, 9],
    ]
)

arr[3, 1] = 10
arr[4, 0] = 5

print(arr)