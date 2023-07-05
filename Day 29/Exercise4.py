import numpy as np

arr = np.arange(1, 34).repeat(6).reshape((-1, 6)).astype('str')
arr = np.char.add(['A', 'B', 'C', 'D', 'E', 'F'], arr)
print(arr)