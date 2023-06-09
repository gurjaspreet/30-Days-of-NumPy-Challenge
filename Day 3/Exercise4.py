import numpy as np


arr = np.array(
    [
        [[3, 2, 4, 0, 1, 3], [5, 0, 4, 4, 4, 1], [3, 2, 4, 1, 1, 4]],
        [[5, 5, 4, 5, 1, 3], [2, 2, 5, 2, 4, 0], [5, 1, 3, 4, 2, 3]],
    ]
)

new_arr = np.ones_like(arr)
print(new_arr)