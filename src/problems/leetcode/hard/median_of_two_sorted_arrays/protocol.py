from typing import Protocol


class SolutionProtocol(Protocol):
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float: ...
