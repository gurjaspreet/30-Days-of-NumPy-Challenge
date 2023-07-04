import numpy as np


A = np.array(
    [
        ['PLW CDR 11B TEN', 'AMC LPP'],
        ['CDR PKO KGH', 'CCC QMK'],
    ],
    dtype='str',
)

result = np.char.split(A, sep=' ')
print(result)