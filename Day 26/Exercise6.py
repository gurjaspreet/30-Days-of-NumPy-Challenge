import numpy as np


u = np.array([1, 0, 0])
v = np.array([0, 1, 0])

lhs = np.linalg.norm(u + v) ** 2
rhs = np.linalg.norm(u) ** 2 + np.linalg.norm(v) ** 2

print(np.allclose(lhs, rhs))