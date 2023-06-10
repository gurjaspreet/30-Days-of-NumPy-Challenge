import numpy as np


A = np.array(
    [
        [False, True, True, False, True],
        [False, False, True, True, True],
        [True, False, False, True, False],
    ]
)
B = np.array(
    [
        [
            [False, True, True, False, True],
            [False, False, True, True, True],
            [True, False, False, True, False],
        ]
    ]
)
C = np.array(
    [
        [[False, True, True, False, True]],
        [[False, False, True, True, True]],
        [[True, False, False, True, False]],
    ]
)
D = np.array([True, False])

print(A.ndim)
print(B.ndim)
print(C.ndim)
print(D.ndim)