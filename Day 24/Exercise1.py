import numpy as np


np.random.seed(10)
arr = np.random.randint(low=1, high=10, size=(3, 5))

result = np.unique(arr)
print(result)