import numpy as np


accumulation_factors = np.array(
    [
        [1.03, 1.035, 1.037],
        [1.037, 1.035, 1.03],
        [1.02, 1.05, 1.028],
        [1.01, 1.023, 1.088],
    ]
)

result = np.prod(accumulation_factors, axis=1).round(5)

print(result)