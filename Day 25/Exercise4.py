import numpy as np


arr = np.array(
    [
        [5, 8, 16],
        [4, 1, 8],
        [-4, 4, -11],
    ]
)

eig_val, eig_vec = np.linalg.eig(arr)
print(eig_val)
print(eig_vec)