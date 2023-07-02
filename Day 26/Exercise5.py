import numpy as np


v1 = np.array([1, 0, 0])
v2 = np.array([0, 1, 0])

angle = np.arccos(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)))
print(np.degrees(angle))