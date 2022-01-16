class Polygon:
    sides = None

    def __init_subclass__(cls):
        super().__init_subclass__()
        if cls.sides is None or cls.sides < 3:
            raise ValueError("Polygon needs at least 3 sides")


class Filled:
    color = None

    def __init_subclass__(cls):
        super().__init_subclass__()
        allowed_colors = ("red", "green", "blue")

        if cls.color is None or cls.color not in allowed_colors:
            raise ValueError(f"Color has to be one of {allowed_colors}")


class Hexagon(Polygon):
    sides = 6


class RedHexagon(Polygon, Filled):
    sides = 6
    color = "red"


class WrongColorHexagon(Polygon, Filled):
    sides = 6
    color = "yellow"


class Wrong(Polygon):
    sides = 2
