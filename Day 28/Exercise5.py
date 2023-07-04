import numpy as np


A = np.array(
    [
        ['#summer#time#mood', '#vibe'],
        ['#sport#time', '#good#time'],
        ['#event#summer', '#fast#move'],
    ]
)

count = np.char.count(A, 'time')
print(count)