import numpy as np


A = np.array(
    [
        [9, 7, 8, 6, 1, 8, 7, 0, 3, 5],
        [0, 5, 2, 7, 9, 9, 2, 6, 9, 6],
        [1, 0, 7, 3, 6, 1, 0, 3, 1, 6],
        [2, 6, 4, 2, 3, 6, 2, 1, 6, 6],
    ]
)

result = np.add.reduce(A, axis=1)
print(result)