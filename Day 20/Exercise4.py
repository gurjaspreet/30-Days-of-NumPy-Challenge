import numpy as np


probabilities = np.array(
    [
        [0.2, 0.6, 0.1, 0.1],
        [0.1, 0.3, 0.6, 0.0],
        [0.9, 0.0, 0.0, 0.1],
        [0.05, 0.15, 0.8, 0.0],
        [0.2, 0.7, 0.1, 0.0],
    ]
)

result = probabilities.size - np.count_nonzero(probabilities)
print(result)