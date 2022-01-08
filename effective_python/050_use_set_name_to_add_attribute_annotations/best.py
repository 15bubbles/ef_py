from typing import Type


class Field:
    def __init__(self):
        self.name = ""
        self.internal_name = ""

    def __set_name__(self, cls, name):
        self.name = name
        self.internal_name = f"_{name}"

    def __get__(self, instance, cls):
        if instance is None:
            return self

        return getattr(instance, self.internal_name, "")

    def __set__(self, instance, value):
        setattr(instance, self.internal_name, value)


class Customer:
    first_name = Field()
    last_name = Field()
    prefix = Field()
    suffix = Field()


if __name__ == "__main__":
    customer = Customer()
    print(customer.__dict__)
    customer.first_name = "lel"
    print(customer.__dict__)
    print(customer.first_name)
