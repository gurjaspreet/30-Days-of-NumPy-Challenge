import numpy as np

q = np.array([2, 4, -5, 1])
r = np.array([2, 0, -5, 1])

q_roots = np.roots(q)
r_roots = np.roots(r)

print(q_roots)
print(r_roots)