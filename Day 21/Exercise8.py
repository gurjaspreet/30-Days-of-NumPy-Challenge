import numpy as np


arr = np.array(
    [
        [1, 0, 5, 0],
        [6, 6, 6, 6],
        [0, 1, np.nan, 1],
        [5, 6, 3, 5],
        [2, 3, 0, 6],
        [0, 1, 4, 5],
        [0, np.nan, 5, 3],
        [6, 2, 1, 1],
        [0, 5, 5, 0],
        [np.nan, 2, 6, 6],
    ]
)

result = np.argwhere(np.isnan(arr))
print(result)