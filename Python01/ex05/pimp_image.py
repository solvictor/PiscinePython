from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def ft_original(array) -> np.array:
    """Don't do anything"""
    return array


def ft_invert(array) -> np.array:
    """Inverts the color of the image received."""
    return 255 - array


def ft_red(array) -> np.array:
    """Apply a red filter on the received image."""
    red = array.copy()
    red[:, :, 1:] = 0
    return red


def ft_green(array) -> np.array:
    """Apply a green filter on the received image."""
    green = array.copy()
    green[:, :, ::2] = 0
    return green


def ft_blue(array) -> np.array:
    """Apply a blue filter on the received image."""
    blue = array.copy()
    blue[:, :, :2] = 0
    return blue


def ft_grey(array) -> np.array:
    """Apply a grey filter on the received image."""
    grey = np.dot(array, [0.299, 0.587, 0.114])
    return np.stack((grey, grey, grey), axis=-1).astype(np.uint8)


def main():
    """Load landscape.jpg and rotate it"""

    array = ft_load("landscape.jpg")
    if array is None:
        return

    print(array)

    fig = plt.figure(figsize=(10, 6))
    rows, cols = 3, 2

    for i, function in enumerate(
            (
            ft_original,
            ft_invert,
            ft_red,
            ft_green,
            ft_blue,
            ft_grey
            )):
        title = function.__name__[3:].capitalize()
        fig.add_subplot(rows, cols, i + 1)
        plt.imshow(function(array))
        plt.axis("off")
        plt.title(title)

    print(ft_invert.__doc__)
    plt.show()


if __name__ == "__main__":
    main()
