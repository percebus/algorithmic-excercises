from src.problems.leetcode.easy.build_array_from_permutation.protocol import SolutionProtocol


class Solution(SolutionProtocol):
    def buildArray(self, nums: list[int]) -> list[int]:
        reordered_numbers = (nums[v] for v in nums)
        return list(reordered_numbers)


solution = Solution()
