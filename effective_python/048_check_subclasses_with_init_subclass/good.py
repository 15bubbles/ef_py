from typing import Type


class PolygonMeta(type):
    def __new__(mcs: Type["PolygonMeta"], name: str, bases: tuple[Type, ...], class_dict: dict):
        # if it's Polygon base, we don't check
        # if we would, we would get error because of default `None`
        # declared on Polygon base class
        # Polygon is a base class, that only uses `metaclass` and does not
        # inherit from anything
        # if it would, when interpreter would get to `Polygon` definition
        # we would see specified class in `bases`
        if bases:
            if class_dict.get("sides") < 3:
                raise ValueError("Polygon needs at least 3 sides")

        return super().__new__(mcs, name, bases, class_dict)


class FilledMeta(type):
    def __new__(mcs: Type["FilledMeta"], name: str, bases: tuple[Type, ...], class_dict: dict):
        allowed_colors = ("red", "green", "blue")

        if bases:
            if class_dict.get("color") not in allowed_colors:
                raise ValueError(f"Color has to be one of {allowed_colors}")

        return super().__new__(mcs, name, bases, class_dict)


class Polygon(metaclass=PolygonMeta):
    sides = None


class Filled(metaclass=FilledMeta):
    color = None


class Hexagon(Polygon):
    sides = 6


class RedSomething(Filled):
    color = "red"


class WrongPolygon(Polygon):
    sides = 2


class WrongColorSomething(Filled):
    color = "orange"


if __name__ == "__main__":
    ...
