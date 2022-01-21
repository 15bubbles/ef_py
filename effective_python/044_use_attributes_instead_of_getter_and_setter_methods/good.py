class Resistor:
    def __init__(self, ohms: float):
        self.ohms = ohms


if __name__ == "__main__":
    resistor = Resistor(2.0)
    print("before")
    print(resistor.ohms)

    resistor.ohms = 3.0
    print("after")
    print(resistor.ohms)
