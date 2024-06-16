from typing import Any


def NULL_not_found(object: Any) -> int:
    if object and object == object:
        print("Type not Found")
        return 1

    ftype = (
        "Nothing" if object is None else
        "Empty" if object == '' else
        "Fake" if object is False else
        "Zero" if object == 0 else
        "Cheese"
    )
    print(ftype + ":", object, type(object))
    return 0
