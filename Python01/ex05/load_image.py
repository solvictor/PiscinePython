import sys
from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray | None:
    """Get the 2D list of pixels in the image at a given path.
    Supports JPG and JPEG

    Args:
        path (str): path to the image

    Returns:
        list: pixels of the image
    """

    try:
        img = Image.open(path)
        img_array = np.array(img)
        print("The shape of image is:", img_array.shape)
        return img_array

    except FileNotFoundError:
        print("Error: Failed to find the file.", file=sys.stderr)

    except IOError:
        print("Error: Failed to read the image.", file=sys.stderr)

    return None


def main():
    """Test this file's functions"""

    print(ft_load("landscape.jpg"))


if __name__ == "__main__":
    main()
