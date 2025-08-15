from problems.leetcode.easy.reverse_string.protocol import SolutionProtocol


class Solution(SolutionProtocol):
    def reverseString(self, s: list[str]) -> None:
        """
        v1.Solution.reverseString.

        Given an array of characters s, it modifies the same array.

        Parameters
        ----------
        - `s:list[str]`.- An array of string characters.

        Returns
        -------
        `None`
        """
        chars = s
        # FIXME simplify do 1 trip, instead of 2
        inverted = chars[::-1]
        for idx, item in enumerate(inverted):
            s[idx] = item  # type: ignore


solution: SolutionProtocol = Solution()
