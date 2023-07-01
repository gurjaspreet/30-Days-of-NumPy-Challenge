import numpy as np


arr = np.array(
    [
        [-2, 0, 4],
        [5, 2, -1],
        [-4, 2, 4],
    ]
)

det = np.linalg.det(arr)
print(det)