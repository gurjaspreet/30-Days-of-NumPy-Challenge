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

print(A.shape)
print(B.shape)
print(C.shape)