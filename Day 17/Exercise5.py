import numpy as np


A = np.array(
    [
        [0, 1, 5, 7],
        [8, 9, 2, 5],
        [3, 4, 6, 7],
    ]
)

A = np.column_stack((A, np.array([1, 4, 2])))
print(A)