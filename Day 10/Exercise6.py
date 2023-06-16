import numpy as np


prices = np.array(
    [
        [46956.85, 47261.27, 46363.63, 46768.23],
        [46504.95, 47365.6, 46215.3, 47283.29],
        [47386.83, 47386.83, 46453.98, 46509.19],
    ]
)

means = (prices.mean(axis=0)).round(2)

print(means)