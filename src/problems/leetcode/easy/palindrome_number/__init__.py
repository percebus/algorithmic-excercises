from .protocol import SolutionProtocol
from .v1 import Solution

oSolution: SolutionProtocol = Solution()
is_palindrome = oSolution.isPalindrome

__all__ = ["Solution", "is_palindrome"]
