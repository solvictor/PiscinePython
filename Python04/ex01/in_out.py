def square(x: int | float) -> int | float:
    """Square a number

    Args:
        x (int | float): the number

    Returns:
        int | float: the squared number
    """

    return x * x


def pow(x: int | float) -> int | float:
    """Exponent a number by itself

    Args:
        x (int | float): the number

    Returns:
        int | float: the result
    """

    return x**x


def outer(x: int | float, function) -> object:
    """Allows repeated calls to a function using outpout as input

    Args:
        x (int | float): initial input
        function (Callable[[int | float], float]): function to repeat

    Returns:
        object: the function wrapper
    """

    def inner() -> float:
        nonlocal x
        x = function(x)
        return x
    return inner


def main() -> None:
    """Test this file's functions"""

    my_counter = outer(3, square)
    print(my_counter())
    print(my_counter())
    print(my_counter())
    print("---")
    another_counter = outer(1.5, pow)
    print(another_counter())
    print(another_counter())
    print(another_counter())


if __name__ == "__main__":
    main()
