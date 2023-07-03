from numpy.polynomial import Polynomial as P

p = P([4.0, -4.0, 1.0])
q = P([2.0, 6.0, -5.0])
r = p + q
print(r.roots())