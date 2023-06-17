import numpy as np


year1 = np.array([1.03, 1.035, 1.037])
year2 = np.array([1.037, 1.035, 1.04])
year3 = np.array([1.02, 1.05, 1.028])
year4 = np.array([1.01, 1.023, 1.088])

y = np.c_[year1, year2, year3, year4]

print(y)



# https://numpy.org/doc/stable/reference/generated/numpy.c_.html