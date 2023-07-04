import numpy as np


A = np.array(['001', '002', '003'], dtype='str')
B = np.array(['XC', 'YC', 'ZC'], dtype='str')

result = np.char.add(A, B)
print(result)