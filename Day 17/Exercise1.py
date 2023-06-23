import numpy as np


A = np.array([0, 1, 5, 7])
B = np.array([[6, 2, 6, 2], [3, 4, 6, 7]])
C = np.array([[56], [65], [79]])

result = np.vstack((A, B))
result = np.hstack((result, C))
print(result)