import numpy as np


arr = np.array(
    [
        [1, 4, 0, 5, 6],
        [9, 7, 4, 0, 6],
        [1, 9, 6, 7, 9],
        [7, 6, 9, 8, 8],
        [2, 2, 1, 5, 2],
        [9, 7, 5, 5, 9],
        [6, 9, 9, 5, 2],
        [9, 6, 1, 8, 1],
    ],
    dtype='int16',
)

unique_elements, element_count = np.unique(arr, return_counts = True)
unique_elements = unique_elements.reshape((-1, 1))
result = np.column_stack((unique_elements, element_count))
print(result)