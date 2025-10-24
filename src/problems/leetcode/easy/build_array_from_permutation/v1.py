from src.problems.leetcode.easy.build_array_from_permutation.protocol import SolutionProtocol


class Solution(SolutionProtocol):
    """Claude Sonnet 4's solution."""

    def buildArray(self, nums: list[int]) -> list[int]:
        # fmt: off
        return [
            nums[nums[i]]
            for i in range(len(nums))]
        # fmt: on


solution = Solution()
