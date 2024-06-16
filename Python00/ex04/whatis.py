import sys

args = sys.argv

try:
    assert len(args) < 3, "more than one argument is provided"

    if len(args) > 1:
        try:
            argument = int(args[1])
            print("I'm", "Odd." if argument & 1 else "Even.")
        except ValueError:
            raise AssertionError("argument is not an integer")
except Exception as error:
    print("AssertionError:", error)
