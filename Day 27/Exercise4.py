import numpy as np

a = np.array(
    [
        [5, -3],
        [1, -2]
    ]
)
b = np.array([21, 7])

s = np.linalg.solve(a, b)
print(f'x = {s[0]:.2f}\ny = {s[1]:.2f}')
