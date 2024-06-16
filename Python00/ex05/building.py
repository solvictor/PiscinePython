import sys


def main(string):
    """Compute the number of different types of characters in a given string

    Args:
        string (str): string to compute
    """

    if not string:
        print("Enter some text:")
        string = sys.stdin.readline()

    upper = lower = punctuation = spaces = digits = 0
    for char in string:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        elif char.isspace():
            spaces += 1
        elif char.isdigit():
            digits += 1
        else:
            punctuation += 1

    print(
        f"The text contains {len(string)} characters:",
        f"{upper} upper letters",
        f"{lower} lower letters",
        f"{punctuation} punctuation marks",
        f"{spaces} spaces",
        f"{digits} digits",
        sep="\n")


if __name__ == "__main__":
    try:
        args = sys.argv
        assert len(args) < 3, "too many arguments"

        main(args[1] if len(args) > 1 else None)
    except AssertionError as error:
        print("AssertionError:", error)
