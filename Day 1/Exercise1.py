'''  
Exercise 1

Using NumPy create a 5x5 array filled with zeros (set data type to int16) and assign it to a variable named arr. In response, print this array to the console.

Expected output:

    [[0 0 0 0 0]
     [0 0 0 0 0]
     [0 0 0 0 0]
     [0 0 0 0 0]
     [0 0 0 0 0]]

Tip: Use the np.zeros() function.   

'''

import numpy as np
arr = np.zeros((5, 5), int)
print(arr)