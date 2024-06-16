from ft_filter import ft_filter
import sys


def main(string, n):
    """Prints every words of string if it has a len strictly greater than n

    Args:
        string (str): sentence to filter out
        n (int): maximum word length

    Raises:
        AssertionError: If n is not an integer or string contains invalid chars
    """

    try:
        n = int(n)
        if not all(char.isalnum() or char == ' ' for char in string):
            raise ValueError()
    except ValueError:
        raise AssertionError("the arguments are bad")

    print([word for word in ft_filter(lambda w: len(w) > n, string.split())])


if __name__ == "__main__":
    try:
        args = sys.argv
        assert len(args) == 3, "the arguments are bad"

        main(*args[1:])
    except AssertionError as error:
        print("AssertionError:", error)
