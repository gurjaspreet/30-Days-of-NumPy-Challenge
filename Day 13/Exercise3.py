import numpy as np

np.random.seed(30) 
sigma = np.sqrt(5)
mu = 100
arr = sigma * np.random.randn(10, 4) + mu

print(arr)