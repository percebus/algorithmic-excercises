from typing import Optional

# SRC: https://leetcode.com/problems/two-sum/
#
# Given an array of integers nums
# and an integer target,
# return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.

# You can return the answer in any order.


class SolutionInterface:
    """An Interface for the two sum problem Solution class."""

    def twoSum(self, nums: list[int], target: int) -> Optional[tuple[int, int]]:
        """Two Sum

        Parameters
        ----------
            - :param: `nums` (list[int]): An array of integers.
            - :param: `target` (int): A target integer.

        Returns
        -------
            - :result: Optional[tuple[int, int]]: indices of two numbers such that they add up to the target.
        """
        raise NotImplementedError
