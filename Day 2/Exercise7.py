import numpy as np


arr = np.array(
    [
        [False, True, True, False, True],
        [False, False, True, True, True],
    ]
)

new_arr = arr.astype('int8')
print(new_arr)