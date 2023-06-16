import numpy as np


arr = np.array(
    [
        [2, 2, 2, 2, 0, 1, 0, 2, 1, 2],
        [2, 1, 0, 0, 0, 0, 0, 2, 1, 0],
        [2, 0, 2, 0, 2, 2, 2, 2, 2, 2],
        [2, 1, 1, 2, 2, 0, 0, 2, 2, 0],
        [0, 1, 0, 2, 0, 2, 0, 0, 0, 1],
    ]
)

print(arr.size - np.count_nonzero(arr))

# print(np.count_nonzero(arr == 0))
# https://stackoverflow.com/questions/42916330/efficiently-count-zero-elements-in-numpy-array