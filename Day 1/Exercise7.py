import numpy as np

arr = np.array(
    [
        ['4', '3', '6', '2', '1'],
        ['7', '2', '1', '2', '6'],
    ],
    dtype='<U1',
)
arr = arr.astype('float16')

print(arr)