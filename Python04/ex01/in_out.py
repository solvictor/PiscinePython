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
    """_summary_

    Args:
        x (int | float): _description_
        function (_type_): _description_

    Returns:
        object: _description_
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
# TODO Comment