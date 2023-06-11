import numpy as np


image1 = np.random.randint(
    low=0,
    high=256,
    size=(200, 300, 3),
    dtype=np.uint8,
)
image2 = np.random.randint(
    low=0,
    high=256,
    size=(200, 300, 3),
    dtype=np.uint8,
)

image1 = np.expand_dims(image1, axis=0)
image2 = np.expand_dims(image2, axis=0)

images = np.concatenate([image1, image2], axis = 0)

# print(images.shape)