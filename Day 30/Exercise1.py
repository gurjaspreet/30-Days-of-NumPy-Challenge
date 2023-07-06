import numpy as np


A = np.array(
    [
        [4, 3, 6],
        [5, 2, 7],
        [8, 3, 10],
        [-3, 4, 2],
    ]
)

def myfunc(arr):
    return np.max(arr) - np.min(arr)

result = np.apply_along_axis(myfunc, axis=1, arr = A)
print(result)