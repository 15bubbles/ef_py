class Resistor:
    def __init__(self, ohms: float):
        self._ohms = ohms

    @property
    def ohms(self) -> float:
        return self._ohms

    @ohms.setter
    def ohms(self, ohms: float) -> None:
        if ohms <= 0:
            raise ValueError("Value for `ohms` has to be grater than 0")

        self._ohms = ohms


if __name__ == "__main__":
    resistor = Resistor(2.0)
    print("before")
    print(resistor.ohms)

    resistor.ohms = 3.0
    print("after")
    print(resistor.ohms)

    print("trying to set inappropriate value")
    resistor.ohms = -1.0
