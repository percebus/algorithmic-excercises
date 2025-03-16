from typing import Protocol, runtime_checkable

# SRC: https://leetcode.com/problems/palindrome-number/
#
# Given an integer x, return true if x is palindrome integer.
# An integer is a palindrome when it reads the same backward as forward.
# For example, 121 is a palindrome while 123 is not.


@runtime_checkable  # NOTE: Allows for isinstance check.
class SolutionProtocol(Protocol):
    def isPalindrome(self, number: int) -> bool:
        """
        SolutionProtocol.isPalindrome.

        Given an integer x, return true if x is palindrome integer.

        Parameters
        ----------
            - `number:int`.- An integer x.

        Returns
        -------
            `bool`.-
                - `True` when it reads the same backward as forward.
                - Otherwise `False`.
        """
        ...  # pylint: disable=unnecessary-ellipsis
