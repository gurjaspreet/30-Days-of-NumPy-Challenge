import numpy as np

arr = np.array(
    [
        [ 0,  1,  2,  3],
        [ 4,  5,  6,  7],
        [ 8,  9, 10, 11]
    ]
)
np.save('array.npy', arr)

arr2 = np.load('array.npy')
print(arr2)