import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generate an id

    Returns:
        str: generated id
    """

    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """Represents a student"""

    name: str
    surname: str
    active: bool = field(default=True)
    login: str = field(init=False)
    id: str = field(init=False, default_factory=generate_id)

    def __post_init__(self):
        """Set uninitializable attributes"""
        self.login = self.name[0] + self.surname


def main() -> None:
    """Test this file's functions"""

    student = Student(name="Edward", surname="agle")
    print(student)

    # Should error
    student = Student(name="Edward", surname="agle", id="toto")
    print(student)


if __name__ == "__main__":
    main()
