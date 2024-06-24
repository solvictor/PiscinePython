from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Representing the King."""

    def __init__(self, first_name, is_alive=True):
        """Create a King."""
        super().__init__(first_name, is_alive)

    def set_eyes(self, color):
        """Setter for eyes."""
        self.eyes = color

    def get_eyes(self):
        """Getter for eyes."""
        return self.eyes

    def set_hairs(self, color):
        """Setter for hairs."""
        self.hairs = color

    def get_hairs(self):
        """Getter for hairs."""
        return self.hairs


def main():
    """Test this file's classes"""

    Joffrey = King("Joffrey")
    print(Joffrey.__dict__)
    Joffrey.set_eyes("blue")
    Joffrey.set_hairs("light")
    print(Joffrey.get_eyes())
    print(Joffrey.get_hairs())
    print(Joffrey.__dict__)


if __name__ == "__main__":
    main()
