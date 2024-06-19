from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def main():
    """Load animal.jpgs an zoom it in"""

    pixels = ft_load("animal.jpeg")
    if pixels is None:
        return

    print(pixels)

    width = pixels.shape[1]
    height = pixels.shape[0]
    center_x = width // 2
    center_y = height // 2
    zoom_factor = 0.52
    half_square = round(min(height, width) * 0.5 * zoom_factor)
    zoomed = pixels[
        center_y - half_square: center_y + half_square,
        center_x - half_square: center_x + half_square
    ]

    zoomed = np.dot(zoomed, [0.299, 0.587, 0.114])

    print("New shape after slicing:", zoomed.shape)
    print(zoomed)

    plt.imshow(zoomed, cmap="gray")
    plt.show()


if __name__ == "__main__":
    main()
