import numpy as np

w = np.array([0, 4, 5, 1])
q = np.array([2, 4, -5, 1])

print(np.polyadd(w, q))
print(np.polysub(w, q))
print(np.polymul(w, q))
print(np.polyadd(w, 2 * q))