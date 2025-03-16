from .protocol import SolutionProtocol


# NOTE: Look mom, no inheritance!
class Solution:  # SolutionProtocol
    def isPalindrome(self, number: int) -> bool:
        """
        Solution.isPalindrome

        Given an integer x, return true if x is palindrome integer.
        An integer is a palindrome when it reads the same backward as forward.

        Parameters
        ----------
            - :param: `number` (int): An integer x.

        Returns
        -------
            - :result: (bool)
                `True` when it reads the same backward as forward.
                Otherwise `False`.
        """
        str1 = str(number)
        str2 = str1[::-1]
        return str1 == str2


solution: SolutionProtocol = Solution()
