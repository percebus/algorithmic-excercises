import abc

# SRC: https://leetcode.com/problems/roman-to-integer/


# NOTE: Formal 'interface' (abstract base class) with no implementation
class SolutionBase(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass: type) -> bool:
        attribute_names = ["romanToInt"]
        attributes = (getattr(subclass, attribute, None) for attribute in attribute_names)
        if not all(attributes):
            return False

        if not all(callable(attribute) for attribute in attributes):
            return False

        return True

    @abc.abstractmethod
    def romanToInt(self, string: str) -> int:
        raise NotImplementedError
