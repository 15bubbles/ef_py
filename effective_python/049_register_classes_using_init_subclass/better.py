import json
from dataclasses import asdict, dataclass
from typing import Any


# we could use TypedDict here but dataclasses give us some easy way
# of validating if user provided proper fields to serialized object,
# and didn't give anything excessive
@dataclass
class SerializedObject:
    cls: str
    args: tuple[Any, ...]


class SerializedException(Exception):
    ...


class ClassNotSerializable(SerializedException):
    ...


class InvalidSerializationFormat(SerializedException):
    ...


_CLS_REGISTRY: dict[str, type] = {}


def _register_class(target_class: type) -> None:
    _CLS_REGISTRY[target_class.__name__] = target_class


class Serializable:
    def __init__(self, *args):
        self.args = args

    def __repr__(self) -> str:
        args = ", ".join([str(arg) for arg in self.args])
        return f"{self.__class__.__name__}({args})"

    # using __init_subclass__ allows us to create this functionality
    # with less code because we don't need metaclass
    # also it seems less confusing without presence of metaclass
    def __init_subclass__(cls) -> None:
        super.__init_subclass__()
        _register_class(cls)

    def serialize(self) -> str:
        data = SerializedObject(
            cls=self.__class__.__name__,
            args=self.args,
        )
        return json.dumps(asdict(data))


class Point2D(Serializable):
    def __init__(self, x: float, y: float):
        super().__init__(x, y)
        self.x = x
        self.y = y


class Point3D(Serializable):
    def __init__(self, x: float, y: float, z: float):
        super().__init__(x, y, z)
        self.x = x
        self.y = y
        self.z = z


# in real world, under ideal circumstances, this should support versioning
def deserialize(data: str) -> Serializable:
    deserialized_data = json.loads(data)

    try:
        serialized_object = SerializedObject(**deserialized_data)
    except TypeError as e:
        raise InvalidSerializationFormat(
            "Invalid serialization format, object can't be properly deserialized"
        ) from e

    # for now we can extract for readability, but if the interface
    # is getting extended, we should rather access attributes directly
    cls_name = serialized_object.cls
    args = serialized_object.args

    target_class = _CLS_REGISTRY.get(cls_name)
    if target_class is None:
        raise ClassNotSerializable(f"Class '{cls_name}' does not support serialization")

    return target_class(*args)


if __name__ == "__main__":
    print("=== Registered classes")
    print(_CLS_REGISTRY)

    point_2d = Point2D(1, 2)
    point_3d = Point2D(3, 4)
    print(point_2d)
    print(point_3d)

    print("=== Serializing")
    serialized_point_2d = point_2d.serialize()
    serialized_point_3d = point_3d.serialize()
    print("Serialized:")
    print(serialized_point_2d)
    print(serialized_point_3d)

    print("=== Deserializing")
    deserialized_point_2d = deserialize(serialized_point_2d)
    deserialized_point_3d = deserialize(serialized_point_3d)
    print("Deserialized:")
    print(deserialized_point_2d)
    print(deserialized_point_3d)
