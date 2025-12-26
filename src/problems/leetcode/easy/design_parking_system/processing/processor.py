from dataclasses import dataclass
from typing import Any, ClassVar, Type

from problems.leetcode.easy.design_parking_system.processing.protocol import ProcessorProtocol
from problems.leetcode.easy.design_parking_system.v2 import ParkingSystem


@dataclass
class Processor(ProcessorProtocol):
    classes: ClassVar[dict[str, Type[Any]]] = {
        "ParkingSystem": ParkingSystem,
    }

    def create_instance(self, class_name: str, arguments: list[Any]) -> Any:
        SomeClass = self.classes[class_name]
        return SomeClass(*arguments)

    def process(self, invoker_names: list[str], arguments: list[Any]) -> list[Any]:
        zipped = zip(invoker_names, arguments)

        first_entry = next(zipped)
        class_name, init_args = first_entry
        instance = self.create_instance(class_name, init_args)
        results = [None]

        for method_name, args in zipped:
            method = getattr(instance, method_name)
            result = method(*args)
            results.append(result)

        return results
