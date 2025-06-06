from hamcrest import assert_that, equal_to

from .solution import solution


def test(nums1: list[int], nums2: list[int], expected: float) -> None:
    result = solution.findMedianSortedArrays(nums1, nums2)
    assert_that(result, equal_to(expected))
    print("✅", end="")


def run() -> None:
    # Example 1:
    # - Input: nums1 = [1,3], nums2 = [2]
    # - Output: 2.00000
    # - Explanation: merged array = [1,2,3] and median is 2.
    test([1, 3], [2], expected=2)

    # Example 2:
    # - Input: nums1 = [1,2], nums2 = [3,4]
    # - Output: 2.50000
    # - Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
    test([1, 2], [3, 4], expected=2.5)

    test([1, 2, 3, 4, 5], [], expected=3)


if __name__ == "__main__":
    run()
