import numpy as np


accumulation_factors = np.array(
    [
        [1.03, 1.085, 1.037],
        [1.037, 1.035, 1.04],
        [1.02, 1.05, 1.028],
        [1.01, 1.023, 1.088],
    ]
)

accumulation_factors[accumulation_factors > 1.05] = 1.05
print(accumulation_factors)