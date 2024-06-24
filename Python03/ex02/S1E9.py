from abc import ABC, abstractmethod


class Character(ABC):
    """Character class"""

    def __init__(self, first_name: str, is_alive=True) -> None:
        """Create a Character named first_name

        Args:
            first_name (str): Name of the character
            is_alive (bool, optional): State of life. Defaults to True.
        """
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self) -> None:
        """Kills the Character"""
        pass


class Stark(Character):
    """Implementation of Character"""

    def die(self) -> None:
        """Kills the Stark"""
        self.is_alive = False


def main():
    """Test this file's classes"""

    Ned = Stark("Ned")
    print(Ned.__dict__)
    print(Ned.is_alive)
    Ned.die()
    print(Ned.is_alive)
    print(Ned.__doc__)
    print(Ned.__init__.__doc__)
    print(Ned.die.__doc__)
    print("---")
    Lyanna = Stark("Lyanna", False)
    print(Lyanna.__dict__)

    # hodor = Character("hodor") # Must produce error


if __name__ == "__main__":
    main()
