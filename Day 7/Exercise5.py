import numpy as np


np.random.seed(42)
arr = np.random.randn(10, 8)
arr = arr.round(3)

print(arr)