import numpy as np


np.random.seed(42)
arr = np.random.randint(low=0, high=2, size=(10, 6))

result = np.count_nonzero(arr)
print(result)