import numpy as np


A = np.array([4, 5, 1, -4])
B = np.array([3, -6, 7, 9])

def add_abs(a, b):
    return abs(a) + abs(b)
    
add_abs = np.frompyfunc(add_abs, 2, 1)
print(add_abs(A, B))