import numpy as np


votes = np.array(['yes', 'no', 'yes', 'no', np.nan, 'yes', 'yes'])

unique_elements, element_count = np.unique(votes, return_counts=True)
print(unique_elements)
print(element_count)