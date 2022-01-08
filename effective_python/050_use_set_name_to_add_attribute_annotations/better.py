from typing import Type


class Field:
    def __init__(self):
        self.name = ""
        self.internal_name = ""

    def __get__(self, instance, instance_type):
        if instance is None:
            return self

        return getattr(instance, self.internal_name, "")

    def __set__(self, instance, value):
        setattr(instance, self.internal_name, value)


class Meta(type):
    def __new__(cls: Type, name: str, bases: tuple[Type], class_dict: dict):
        for key, value in class_dict.items():
            if isinstance(value, Field):
                value.name = key
                value.internal_name = f"_{key}"

        cls = type.__new__(cls, name, bases, class_dict)
        return cls


class DatabaseRow(metaclass=Meta):
    ...


class Customer(DatabaseRow):
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
