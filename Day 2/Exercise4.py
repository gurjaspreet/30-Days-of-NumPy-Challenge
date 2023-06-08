import numpy as np

arr = np.array(
    [
        [4.99, 3.49, 9.99],
        [1.99, 9.99, 14.99],
        [14.99, 2.39, 7.29],
    ]
)

# new_arr = np.zeros(arr.shape, arr.dtype)

new_arr = np.zeros_like(arr)
print(new_arr)