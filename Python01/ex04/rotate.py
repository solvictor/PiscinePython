from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def main():
    """Load animal.jpeg and rotate it"""

    pixels = ft_load("animal.jpeg")
    if pixels is None:
        return

    print(pixels)

    transposed = []
    for column in range(pixels.shape[1]):
        new_line = [pixels[line][column] for line in range(pixels.shape[0])]
        transposed.append(new_line)

    # Grey filter
    transposed = np.dot(transposed, [0.299, 0.587, 0.114])

    print("New shape after Transpose:", transposed.shape)
    print(transposed)

    plt.imshow(transposed, cmap="grey")
    plt.show()


if __name__ == "__main__":
    main()
