from typing import Any


class SomeClass:
    def __init__(self):
        self.exists = 5

    def __getattribute__(self, name: str) -> Any:
        print("== Insidde __getattribute__")

        try:
            value = super().__getattribute__(name)
            print(f"Got `{value=}` to {name=} attribute")
            return value
        except AttributeError:
            # print(f"Couldn't get {name=} attribute")
            # print("Setting something else")
            # setattr(self, name, "Something")
            raise  # raising `AttributeError` determines if __getattr__ will be invoked or not

    def __getattr__(self, name: str) -> Any:
        print("== Inside __getattr__")

        value = "Something"
        print(f"Setting `{value=}` to {name=} attribute")
        setattr(self, name, value)

    def __setattr__(self, name: str, value: Any) -> None:
        print("== Inside __setattr__")
        print(f"Setting {name=}, {value=}")
        super().__setattr__(name, value)


if __name__ == "__main__":
    print("/// Initializing")
    s = SomeClass()

    print("/// Setting attribute")
    s.foo = 5

    print("/// Acessing attribute that does not exist")
    print("    Before")
    print(s.__dict__)
    print(s.lel)
    print("    After")
    print(s.__dict__)
    print(s.lel)
