import numpy as np


A = np.array(
    [
        [2.46532508, 1.38323223, 0.34623312, 1.02251611, 0.16681027],
        [1.65671662, 0.66788961, -0.22994664, -1.12955119, -0.6399626],
        [0.31383052, -1.22583598, -0.22179314, 1.33992631, 0.02930971],
        [1.98538575, 1.4471656, -0.28762941, -1.35931057, -0.04804133],
        [-0.48078734, 0.37775309, 1.61440797, -1.12310404, -0.38872795],
        [0.33234995, 1.13497317, 0.51071441, 0.41429764, 1.34454942],
        [0.49351532, -0.23700418, 0.05728515, -0.70707145, 0.54666484],
        [0.94250041, -2.97959677, 1.21814885, -0.05652072, 0.46088845],
        [0.66237401, -2.29510333, -1.19592931, -0.33310116, -0.79139077],
        [0.27417278, -0.51490992, -1.7110712, 0.61229731, 1.10012937],
    ]
)

A1, A2 = np.split(A, 2, axis=0)

print(A1)
print(A2)