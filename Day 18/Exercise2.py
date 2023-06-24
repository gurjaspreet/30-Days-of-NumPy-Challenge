import numpy as np


image = np.random.randint(
    low=0,
    high=256,
    size=(200, 300),
    dtype=np.uint8,
)

image_sorted = np.sort(image, axis=1)