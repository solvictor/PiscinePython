class calculator:

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        dot = sum(a * b for a, b in zip(V1, V2))
        print("Dot product is:", dot)

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        add = [float(a + b) for a, b in zip(V1, V2)]
        print("Add Vector is :", add)

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        sous = [float(a - b) for a, b in zip(V1, V2)]
        print("Sous Vector is:", sous)


def main():
    """Test this file's classes"""

    a = [5, 10, 2]
    b = [2, 4, 3]
    calculator.dotproduct(a, b)
    calculator.add_vec(a, b)
    calculator.sous_vec(a, b)


if __name__ == "__main__":
    main()
