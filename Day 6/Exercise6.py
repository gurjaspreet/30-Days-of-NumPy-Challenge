import numpy as np


arr = np.array(
    [
        [1, 0, 5, 0],
        [6, 6, 6, 6],
        [0, 1, 4, 1],
        [5, 6, 3, 5],
        [2, 3, 0, 6],
        [0, 1, 4, 5],
        [0, 4, 5, 3],
        [6, 2, 1, 1],
        [0, 5, 5, 0],
        [4, 2, 6, 6],
    ]
)

result = np.where(arr == 0)
indices = list(zip(result[0], result[1]))
print(indices)