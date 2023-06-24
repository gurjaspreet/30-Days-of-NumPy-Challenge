import numpy as np


arr = np.array(
    [
        [4, 3, 6],
        [5, 2, 7],
        [8, 3, 10],
        [-3, 4, 2],
    ]
)

def myfunc(arr):
    return np.amax(arr) - np.amin(arr)

diff = np.apply_along_axis(myfunc, axis=0, arr=arr)
print(diff)