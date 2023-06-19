import numpy as np

np.random.seed(42)
image = np.random.randint(0, 256, (200, 300, 3), 'uint8')

print(image)