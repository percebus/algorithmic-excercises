from typing import Optional

# SRC: https://leetcode.com/problems/two-sum/
#
# Given an array of integers nums
# and an integer target,
# return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.

# You can return the answer in any order.


def two_sum(nums: list[int], target: int) -> Optional[list[int]]:
    """Two Sum

    Args:
        nums (list[int]): An array of integers.
        target (int): A target integer.

    Returns:
        Optional[list[int]]: indices of two numbers such that they add up to the target.
    """

    for idx1, value1 in enumerate(nums):
        for idx2, value2 in enumerate(nums):
            # "you may not use the same element twice"
            if idx1 == idx2:
                continue

            # "return indices of the two numbers such that they add up to target"
            if value1 + value2 == target:
                return [idx1, idx2]

    return None
