from typing import Any


def callLimit(limit: int):
    """Limit the number of times you can call a function

    Args:
        limit (int): call limit

    Returns:
        function: limited function
    """

    count = 0

    def callLimiter(function):

        def limit_function(*args: Any, **kwds: Any):
            nonlocal count
            if count >= limit:
                print("Error:", function, "call too many times")
                return None

            count += 1
            return function(*args, **kwds)

        return limit_function

    return callLimiter


def main() -> None:
    """Test this file's functions"""

    @callLimit(3)
    def f():
        print("f()")

    @callLimit(1)
    def g():
        print("g()")

    for _ in range(3):
        f()
        g()


if __name__ == "__main__":
    main()
