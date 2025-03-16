from math import floor

from src.problems.leetcode.easy.reverse_string.protocol import SolutionProtocol


class Solution(SolutionProtocol):
    def reverseString(self, s: list[str]) -> None:
        """
        v2.Solution.reverseString.

        Given an array of characters s, it modifies the same array.

        Parameters
        ----------
        - `s:list[str]`.- An array of string characters.

        Returns
        -------
        `None`
        """
        chars = s
        size: int = len(chars)
        top: int = size - 1
        mid: int = floor(size / 2)
        for idx in range(mid):
            char_a: str = chars[idx]
            char_b: str = chars[top - idx]
            chars[top - idx] = char_a
            chars[idx] = char_b


solution: SolutionProtocol = Solution()
