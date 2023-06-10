import numpy as np


np.random.seed(20)
arr = np.array(
    [
        [3, 4, 0, 5, 6],
        [9, 7, 4, 0, 6],
        [1, 9, 6, 7, 9],
        [7, 6, 9, 8, 8],
        [2, 2, 1, 5, 2],
        [9, 7, 5, 5, 9],
        [6, 9, 9, 5, 2],
        [9, 6, 1, 8, 1],
    ],
    dtype='float64',
)

print('float64:', arr.nbytes)
print('float32:', arr.astype('float32').nbytes)
print('int16:', arr.astype('int16').nbytes)