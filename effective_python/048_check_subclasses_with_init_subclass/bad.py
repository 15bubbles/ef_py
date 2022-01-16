# it can be quite bad when were trying to use two different metaclasses
# to join two different validations
from typing import Type


class PolygonMeta(type):
    def __new__(mcs: Type["PolygonMeta"], name: str, bases: tuple[Type, ...], class_dict: dict):
        if bases:
            if (sides := class_dict.get("sides")) is None or sides < 3:
                raise ValueError("Polygon needs at least 3 sides")

        return super().__new__(mcs, name, bases, class_dict)


class FilledMeta(type):
    def __new__(mcs: Type["FilledMeta"], name: str, bases: tuple[Type, ...], class_dict: dict):
        allowed_colors = ("red", "green", "blue")

        if bases:
            if (color := class_dict.get("color")) is None or color not in allowed_colors:
                raise ValueError(f"Color has to be one of {allowed_colors}")

        return super().__new__(mcs, name, bases, class_dict)


class Polygon(metaclass=PolygonMeta):
    sides = None


class Filled(metaclass=FilledMeta):
    color = None


# we will get a bit of an unclear error message
class RedPentagon(Polygon, Filled):
    sides = 5
    color = "red"


if __name__ == "__main__":
    ...
