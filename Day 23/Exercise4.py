import numpy as np


np.random.seed(42)
arr = np.random.randint(10, size=(100, 30))

np.set_printoptions(edgeitems=10)
print(arr)