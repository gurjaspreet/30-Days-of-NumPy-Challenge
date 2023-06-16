import numpy as np


arr = np.array(
    [
        [3, 4, 2, 3, 4, 3, 4, 2],
        [2, 4, 2, 1, 2, 3, 1, 4],
        [4, 1, 2, 4, 2, 4, 1, 4],
        [4, 1, 2, 4, 4, 2, 1, 4],
        [2, 3, 3, 4, 2, 2, 1, 4],
    ]
)

print(arr.cumprod(axis=1))



# for i in range(len(arr)):
#     for j in range(1, len(arr[i])):
#         arr[i, j] *= arr[i, j-1]
# print(arr)