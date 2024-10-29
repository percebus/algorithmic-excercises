from typing import Optional

from .base import SolutionInterface


class Solution(SolutionInterface):
    def twoSum(self, nums: list[int], target: int) -> Optional[tuple[int, int]]:
        for idx1, value1 in enumerate(nums):
            for idx2, value2 in enumerate(nums):
                # "you may not use the same element twice"
                if idx1 == idx2:
                    continue

                # "return indices of the two numbers such that they add up to target"
                if value1 + value2 == target:
                    return (idx1, idx2)

        return None


solution = Solution()
