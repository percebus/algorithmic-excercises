# ruff: noqa
# pylint: skip-file


from problems.leetcode.hard.median_of_two_sorted_arrays.protocol import SolutionProtocol


class Solution(SolutionProtocol):
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        x, y = len(nums1), len(nums2)
        low, high = 0, x

        while low <= high:
            partitionX = (low + high) // 2
            partitionY = (x + y + 1) // 2 - partitionX

            # Handle edge cases for partitions
            maxX = float("-inf") if partitionX == 0 else nums1[partitionX - 1]
            minX = float("inf") if partitionX == x else nums1[partitionX]

            maxY = float("-inf") if partitionY == 0 else nums2[partitionY - 1]
            minY = float("inf") if partitionY == y else nums2[partitionY]

            # Check if we have found the correct partition
            if maxX <= minY and maxY <= minX:
                # If the total length is even
                if (x + y) % 2 == 0:
                    return (max(maxX, maxY) + min(minX, minY)) / 2
                # If the total length is odd
                else:
                    return max(maxX, maxY)
            elif maxX > minY:
                high = partitionX - 1
            else:
                low = partitionX + 1

        raise ValueError("Input arrays are not sorted or invalid")


solution = Solution()
