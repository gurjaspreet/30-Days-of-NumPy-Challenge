import numpy as np

string_data = '4 2 6 2 7 10 6 2 14'

arr = np.array(string_data.split(), dtype='int16')
# arr = np.fromstring(string_data, dtype='int16', sep=' ')

print(arr)