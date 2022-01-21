class ResistorBase:
    def __init__(self, ohms: float):
        self.ohms = ohms


class Resistor(ResistorBase):
    def __init__(self, ohms: float):
        super().__init__(ohms)

    @property
    def ohms(self) -> float:
        return self._ohms

    @ohms.setter
    def ohms(self, ohms) -> None:
        if ohms <= 0:
            raise ValueError("Value for `ohms` has to be greater than 0")

        self._ohms = ohms


class FixedResistor(ResistorBase):
    def __init__(self, ohms: float):
        super().__init__(ohms)

    @property
    def ohms(self):
        return self._ohms
    
    @ohms.setter
    def ohms(self, ohms: float) -> None:
        if hasattr(self, "_ohms"):
            raise AttributeError("Can't set attribute")

        self._ohms = ohms


if __name__ == "__main__":
    # this will call setter to check if proper value has been provided at init
    resistor = Resistor(1.0)
    print(resistor.ohms)

    resistor2 = FixedResistor(1.0)
    resistor2.ohms = 3.0
