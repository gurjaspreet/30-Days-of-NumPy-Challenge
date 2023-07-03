import numpy as np

a = np.array(
    [
        [1, 1, 1],
        [2, 1, 5],
        [1, -1, -1]
    ]
)
b = np.array([1, 0, 0])

x = np.linalg.solve(a, b)
print(f'x = {x[0]:.2f}\ny = {x[1]:.2f}\nz = {x[2]:.2f}')