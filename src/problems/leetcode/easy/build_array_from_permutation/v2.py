from src.problems.leetcode.easy.build_array_from_permutation.protocol import SolutionProtocol


class Solution(SolutionProtocol):
    def buildArray(self, nums: list[int]) -> list[int]:
        num_of_numbers: int = len(nums)
        ordered_numbers = range(num_of_numbers)
        numbers = (nums[i] for i in ordered_numbers)
        reordered_numbers = (nums[i] for i in numbers)
        return list(reordered_numbers)

solution = Solution()
