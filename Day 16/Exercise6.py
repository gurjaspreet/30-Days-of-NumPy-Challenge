import numpy as np


def shift(arr, n):
    if n > 0:
        temp = np.array([np.nan for i in range(n)], dtype=arr.dtype)
        arr = np.concatenate((temp, arr[:-n]), axis=0)
    elif n < 0:
        n = np.abs(n)
        temp = np.array([np.nan for i in range(n)], dtype=arr.dtype)
        arr = np.concatenate((arr[n:], temp), axis=0)
    return arr