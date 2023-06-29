import numpy as np


A = np.array(
    [
        [-4, 3, 0, 1, -5],
        [6, -4, -2, 1, 3],
    ]
)

result = np.sign(A)
print(result)