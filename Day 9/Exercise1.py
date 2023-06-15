import numpy as np


arr = np.array(
    [
        [6, 7, 7, 3, 9],
        [7, 4, 8, 4, 0],
        [1, 5, 3, 2, 4],
        [7, 8, 9, 8, 2],
    ]
)

arr = arr.reshape(5, -1)

print(arr)