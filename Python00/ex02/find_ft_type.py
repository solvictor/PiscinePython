from typing import Any


def all_thing_is_obj(object: Any) -> int:
    stype = str(type(object))
    if isinstance(object, int):
        print("Type not found")
    elif isinstance(object, str):
        print(object, "is in the kitchen :", stype)
    else:
        print(stype.split("'")[-2].capitalize(), ":", stype)
    return 42
