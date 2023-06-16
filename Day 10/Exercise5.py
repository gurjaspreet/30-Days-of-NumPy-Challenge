import numpy as np


arr = np.array(
    [
        [0.9, 0.01, 0.09],
        [0.1, 0.3, 0.6],
        [0.1, 0.2, 0.7],
    ]
)

max_val = arr.max(axis=1)

print(max_val)