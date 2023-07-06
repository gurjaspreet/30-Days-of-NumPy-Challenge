import numpy as np


A = np.array([4, 5, 1, -4])
B = np.array([[3, 6, 7, 9], [-1, 2, 5, 4]])

def add_three(anything):
    return anything + 3
    
add_three = np.frompyfunc(add_three, 1, 1)
 
print(add_three(A))
print(add_three(B))