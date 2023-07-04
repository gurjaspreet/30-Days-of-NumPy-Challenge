import numpy as np


A = np.array([['#summer#time#mood'], ['#sport#time']])

result = np.char.strip(np.char.replace(A, '#', ' '))
print(result)