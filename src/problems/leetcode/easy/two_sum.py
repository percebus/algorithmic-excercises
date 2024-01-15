# SRC: https://leetcode.com/problems/two-sum/
#
# Given an array of integers nums
# and an integer target,
# return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.
#
# You can return the answer in any order.
from hamcrest import assert_that, equal_to


def two_sum(nums, target):
    for idx1, value1 in enumerate(nums):
        for idx2, value2 in enumerate(nums):
            # "you may not use the same element twice"
            if idx1 == idx2:
                continue

            # "return indices of the two numbers such that they add up to target"
            if value1 + value2 == target:
                return [idx1, idx2]

    return None


def test(nums, target, expected=None):
    result = two_sum(nums, target)
    assert_that(result, equal_to(expected))
    print("✅", end="")


def run():
    # Example 1:
    # - Input: nums = [2,7,11,15], target = 9
    # - Output: [0,1]
    # - Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
    test([2, 7, 11, 15], 9, expected=[0, 1])

    # Example 2:
    # - Input: nums = [3,2,4], target = 6
    # - Output: [1,2]
    test([3, 2, 4], 6, expected=[1, 2])

    # Example 3:
    # - Input: nums = [3,3], target = 6
    # - Output: [0,1]
    test([3, 3], 6, expected=[0, 1])

    print("\n")


if __name__ == "__main__":
    run()
