import numpy as np


arr = np.array(
    [
        [
            [0.0, 2.0, 0.5, 1.0],
            [0.0, 2.0, 0.0, 3.0],
            [0.0, 4.0, 0.0, 0.0],
        ],
        [
            [0.0, 0.5, 0.0, 0.2],
            [0.0, 0.4, 0.0, 5.0],
            [0.0, 0.0, 1.0, 0.0],
        ],
    ]
)

np.savetxt('arr1.csv', arr[0], delimiter=',')
np.savetxt('arr2.csv', arr[1], delimiter=',')

arr1 = np.loadtxt('arr1.csv', delimiter=',')
arr2 = np.loadtxt('arr2.csv', delimiter=',')

new_arr = np.c_[[arr1.T, arr2.T]]
print(new_arr)