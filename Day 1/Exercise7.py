'''
Exercise 7

Suppose you have the following NumPy array:

    arr = np.array(
        [
            ['4', '3', '6', '2', '1'],
            ['7', '2', '1', '2', '6'],
        ],
        dtype='<U1',
    )

Change the data type of this array to float16. In response print this array to the console.

Expected output:

    [[4. 3. 6. 2. 1.]
     [7. 2. 1. 2. 6.]]

'''

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