from typing import Protocol, runtime_checkable

"""
SRC: https://leetcode.com/problems/reverse-string/

Write a function that reverses a string.
The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.
"""


@runtime_checkable  # NOTE: Allows for isinstance check.
class SolutionProtocol(Protocol):
    def reverseString(self, s: list[str]) -> None:
        """
        SolutionProtocol.reverseString.

        Given an array of characters s, it modifies the same array.

        Parameters
        ----------
        - `s:list[str]`.- An array of string characters.

        Returns
        -------
        `None`
        """
        ...  # pylint: disable=unnecessary-ellipsis
