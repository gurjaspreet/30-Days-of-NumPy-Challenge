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
    arr[0], arr[-1] = arr[-1], arr[0]
    return arr
    
result = np.apply_along_axis(myfunc, 1, A)
print(result)