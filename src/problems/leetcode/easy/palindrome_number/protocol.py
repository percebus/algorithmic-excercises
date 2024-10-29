from typing import Protocol

# SRC: https://leetcode.com/problems/palindrome-number/
#
# Given an integer x, return true if x is palindrome integer.
# An integer is a palindrome when it reads the same backward as forward.
# For example, 121 is a palindrome while 123 is not.


class SolutionProtocol(Protocol):
    def isPalindrome(self, number: int) -> bool:  # type: ignore
        """
        SolutionProtocol.isPalindrome

        Given an integer x, return true if x is palindrome integer.

        Parameters:
            `number` (`int`): An integer x.

        Returns:
            `bool`:
                `True` or `False`.
        """
