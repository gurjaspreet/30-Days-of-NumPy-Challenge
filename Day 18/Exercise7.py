import numpy as np


A = np.array(
    [
        [563, 996, 272, 400, 487, 581, 117, 749, 434, 815],
        [195, 942, 938, 580, 897, 72, 109, 600, 979, 586],
        [468, 970, 898, 765, 316, 368, 143, 381, 674, 971],
        [963, 733, 548, 247, 779, 170, 830, 665, 692, 502],
        [40, 494, 384, 353, 337, 181, 689, 142, 181, 386],
    ]
)

A[A % 5 == 0] = 0
print(A)