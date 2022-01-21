class Resistor:
    def __init__(self, ohms: float):
        self._ohms = ohms

    def get_ohms(self) -> float:
        return self._ohms
    
    def set_ohms(self, ohms: float) -> None:
        self._ohms = ohms


if __name__ == "__main__":
    resistor = Resistor(2.0)
    print("before")
    print(resistor.get_ohms())

    resistor.set_ohms(3.0)
    print("after")
    print(resistor.get_ohms())
