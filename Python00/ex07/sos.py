import sys


def main(string):
    """Prints string as morse code

    Args:
        string (str): string to convert
    """

    NESTED_MORSE = {
        " ": "/",
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
    }

    print(*map(NESTED_MORSE.get, string.upper()))


if __name__ == "__main__":
    args = sys.argv

    try:
        assert len(args) == 2, "the arguments are bad"

        s = args[1]
        assert all(c.isalnum() or c == ' ' for c in s), "the arguments are bad"

        main(s)
    except AssertionError as error:
        print("AssertionError:", error)
