import numpy as np


arr = np.array(
    [
        [0.98719372, 0.40157794, 0.72824049, 0.20055243],
        [0.58863943, 0.1753418, 0.02128165, 0.78263826],
        [0.33259132, 0.80081786, 0.26790891, 0.53948946],
        [0.00659557, 0.14391722, 0.3477083, 0.14417694],
    ]
)

print(np.diag(arr))