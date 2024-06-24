class calculator:

    def __init__(self, lst) -> None:
        """Allow vector calculations

        Args:
            lst (list): vector to work with
        """

        assert isinstance(lst, list)
        assert all(isinstance(e, (float, int)) for e in lst)
        self.lst = lst

    def __add__(self, object) -> None:
        """Add a number to every elements of the vector

        Args:
            object (float, int): number to add
        """

        assert isinstance(object, (float, int))
        self.lst = [e + object for e in self.lst]
        print(self.lst)

    def __mul__(self, object) -> None:
        """Multiply every elements of the vector by a number

        Args:
            object (float, int): number to multiply
        """

        assert isinstance(object, (float, int))
        self.lst = [e * object for e in self.lst]
        print(self.lst)

    def __sub__(self, object) -> None:
        """Subtract a number to every elements of the vector

        Args:
            object (float, int): number to subtract
        """

        assert isinstance(object, (float, int))
        self.lst = [e - object for e in self.lst]
        print(self.lst)

    def __truediv__(self, object) -> None:
        """Divide every elements of the vector by a number

        Args:
            object (float, int): number to divide
        """

        assert isinstance(object, (float, int))
        assert object != 0
        self.lst = [e / object for e in self.lst]
        print(self.lst)


def main():
    """Test this file's classes"""

    v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v1 + 5
    print("---")
    v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v2 * 5
    print("---")
    v3 = calculator([10.0, 15.0, 20.0])
    v3 - 5
    v3 / 5


if __name__ == "__main__":
    main()
