def slice_me(family: list, start: int, end: int) -> list:
    """Slice a 2D array

    Args:
        family (list): array to slice
        start (int): lower bound
        end (int): upper bound

    Returns:
        list: sliced array
    """

    assert (
        isinstance(family, list) and
        isinstance(start, int) and
        isinstance(end, int)
    )
    assert all(isinstance(sub, list) for sub in family)

    r = len(family)
    c = len(family[0]) if r else 0

    assert all(len(sub) == c for sub in family)

    print("My shape is :", (r, c))
    sliced = family[start:end]
    print("My new shape is :", (len(sliced), c))
    return sliced


def main():
    """Test this file's functions"""

    family = [
        [1.80, 78.4],
        [2.15, 102.7],
        [2.10, 98.5],
        [1.88, 75.2]
    ]

    print(slice_me(family, 0, 2))
    print(slice_me(family, -1, -2))


if __name__ == "__main__":
    main()
