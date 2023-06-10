import numpy as np


A1 = np.array([3, 5, 1, 2, 5, 4])
A2 = np.array([3, 5, 1, 4, 7, 3, 8, 24], dtype=np.int8)
A3 = np.array([3, 5, 1, 6, 2], dtype=np.int16)

dict = {'A1': A1.nbytes, 'A2': A2.nbytes, 'A3': A3.nbytes}

print(min(dict, key=dict.get))