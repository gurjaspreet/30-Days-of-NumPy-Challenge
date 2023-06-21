import numpy as np

arr = np.arange(12, dtype='float').reshape(-1, 4)
np.savetxt('array.txt', arr, fmt='%0.2f')

arr2 = np.loadtxt('array.txt')
print(arr2)