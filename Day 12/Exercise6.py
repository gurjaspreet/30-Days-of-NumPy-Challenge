import numpy as np
 
 
dates = np.arange('2025-01-01', '2025-01-10', dtype='datetime64[D]')

print(np.busday_count(dates[0], dates[-1] + 1))

# https://numpy.org/doc/stable/reference/arrays.datetime.html#np-busday-count