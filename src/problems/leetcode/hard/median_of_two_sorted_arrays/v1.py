import math

"""
SRC: https://leetcode.com/problems/median-of-two-sorted-arrays/

Given two sorted arrays nums1 and nums2
of size m and n respectively,
return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)). # TODO TEST
"""


def find_median(nums1: list[int], nums2: list[int]) -> float:
    nums3 = nums1 + nums2
    nums3.sort()
    size = len(nums3)
    mid = math.ceil(size / 2)
    is_pair = (size % 2) == 0
    idx = mid - 1

    if not is_pair:
        return nums3[idx]

    # implicit else
    return (nums3[idx] + nums3[idx + 1]) / 2
