import numpy as np


dates = np.arange('2025-01', '2025-02', dtype='datetime64[D]')

result = np.array([[day, day + 3] for day in dates])

print(result)