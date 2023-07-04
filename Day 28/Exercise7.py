import numpy as np


filenames = np.array(
    [
        [
            '003_image.jpg',
            '043_image.jpg',
            '060_image.jpg',
            '002_image.png',
        ],
        [
            '098_image.jpg',
            '023_image.png',
            '004_image.jpg',
            '001_image.jpg',
        ],
        [
            '035_image.jpg',
            '055_image.jpg',
            '009_image.png',
            '100_image.jpg',
        ],
    ]
)

idx = np.char.endswith(filenames, '.jpg')
result = filenames[idx]
print(result)