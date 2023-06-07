'''
Exercise 5

Using NumPy, create a 8x8 two-dimensional array - identity matrix with int16 data type and assign it to a variable named arr. In response, print this array to the console as shown below.


Expected output:

    [[1 0 0 0 0 0 0 0]
     [0 1 0 0 0 0 0 0]
     [0 0 1 0 0 0 0 0]
     [0 0 0 1 0 0 0 0]
     [0 0 0 0 1 0 0 0]
     [0 0 0 0 0 1 0 0]
     [0 0 0 0 0 0 1 0]
     [0 0 0 0 0 0 0 1]]

     
Tip: Use the np.eye() function.

'''

import numpy as np

arr = np.eye(8, dtype='int16')
print(arr)