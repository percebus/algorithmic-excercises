# SRC: https://leetcode.com/problems/longest-common-prefix/
#
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string.


# NOTE: Ideally, you would want issubclass(...) to return False
# when the implementing class doesn’t define all of the interface’s abstract methods.
# pylint: disable=E1120 # no-value-for-parameter  # FIXME
class SolutionMeta(type):
    """A Parser metaclass that will be used for parser class creation."""

    def __instancecheck__(cls, instance: object) -> bool:
        return cls.__subclasscheck__(type(instance))

    def __subclasscheck__(cls, subclass: type) -> bool:
        attribute_names = ["longestCommonPrefix"]
        attributes = (getattr(subclass, attribute, None) for attribute in attribute_names)
        if not all(attributes):
            return False

        if not all(callable(attribute) for attribute in attributes):
            return False

        return True


# pylint: enable = E1120


# NOTE: 'Informal Interface'.
class SolutionInterface(metaclass=SolutionMeta):
    """An Interface for LongestCommonPrefix Solution problem."""

    def longestCommonPrefix(self, words: list[str]) -> str:
        """Longest Common Prefix

        Parameters:
            - :param: `words` (list[str]): Different words that might share a common prefix.

        Returns:
            - :result: str:
              - The longest common prefix string amongst an array of strings.
              - If there is no common prefix, it returns an empty string.
        """
        raise NotImplementedError
