import numpy as np

np.random.seed(42)
draw = np.random.choice(range(1, 50), size=6, replace=False)

print(draw)