from typing import Any


def mean(lst):
    """Get a list's mean value

    Args:
        lst (list): the list

    Returns:
        float: the mean
    """

    return sum(lst) / len(lst)


def median(lst):
    """Get a list's median value

    Args:
        lst (list): the list

    Returns:
        float: the median
    """

    return lst[len(lst) // 2]


def quartile(lst):
    """Get a list's quartile values

    Args:
        lst (list): the list

    Returns:
        list[float]: the quartile values
    """

    return [
        float(lst[len(lst) // 4]),
        float(lst[len(lst) * 3 // 4]),
    ]


def var(lst):
    """Get a list's variance

    Args:
        lst (list): the list

    Returns:
        float: the variance
    """

    avg = mean(lst)
    return sum((x - avg) ** 2 for x in lst) / len(lst)


def std(lst):
    """Get a list's standard deviation

    Args:
        lst (list): the list

    Returns:
        float: the standard deviation
    """

    return var(lst) ** 0.5


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """Get a vector's statistics"""

    for arg in args:
        if not isinstance(arg, (int, float)):
            print("ERROR")
            return

    args = sorted(args)
    funcs = {
        f.__name__: f for f in (mean, median, quartile, var, std)
    }

    for name in kwargs.values():
        if name in funcs:
            if args:
                print(name, ':', funcs[name](args))
            else:
                print("ERROR")


def main() -> None:
    """Test this file's functions"""

    ft_statistics(1, 42, 360, 11, 64,
                  toto="mean", tutu="median", tata="quartile")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575,
                  ejfhhe="heheh", ejdjdejn="kdekem")
    print("-----")
    ft_statistics(toto="mean", tutu="median", tata="quartile")


if __name__ == "__main__":
    main()
