import numpy as np


A = np.array(['1', '2', '3'], dtype='str')

result = np.char.zfill(A, 4)
print(result)