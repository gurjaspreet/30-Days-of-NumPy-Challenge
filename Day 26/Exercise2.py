import numpy as np


v1 = np.array([5, -1, 5])
v2 = np.array([3, 1, 0])

result = np.dot(v1, v2.T)
print(result)