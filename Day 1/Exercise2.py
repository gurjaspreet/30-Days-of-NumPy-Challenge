'''
Exercise 2

Using NumPy, create a 10x10 array filled with number 8 (set the data type to float32) and assign it to a variable named arr. In response, print this array to the console as shown below.


Expected output:

    [[8. 8. 8. 8. 8. 8. 8. 8. 8. 8.]
     [8. 8. 8. 8. 8. 8. 8. 8. 8. 8.]
     [8. 8. 8. 8. 8. 8. 8. 8. 8. 8.]
     [8. 8. 8. 8. 8. 8. 8. 8. 8. 8.]
     [8. 8. 8. 8. 8. 8. 8. 8. 8. 8.]
     [8. 8. 8. 8. 8. 8. 8. 8. 8. 8.]
     [8. 8. 8. 8. 8. 8. 8. 8. 8. 8.]
     [8. 8. 8. 8. 8. 8. 8. 8. 8. 8.]
     [8. 8. 8. 8. 8. 8. 8. 8. 8. 8.]
     [8. 8. 8. 8. 8. 8. 8. 8. 8. 8.]]


Tip: Use the np.ones() or np.full() functions.

'''

import numpy as np

# arr = np.ones(shape=(10, 10), dtype='float32') * 8

arr = np.full((10, 10), 8, dtype='float32')
print(arr)