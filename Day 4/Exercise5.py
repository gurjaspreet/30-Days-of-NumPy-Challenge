import numpy as np


A1 = np.array([3, 5, 1])
A2 = np.array([3, 5, 1], dtype=np.int8)
A3 = np.array([3, 5, 1], dtype=np.int16)
A4 = np.array([3, 5, 1], dtype='float')

# print(A1.nbytes)
print(A1.size * A1.itemsize)
print(A2.size * A2.itemsize)
print(A3.size * A3.itemsize)
print(A4.size * A4.itemsize)