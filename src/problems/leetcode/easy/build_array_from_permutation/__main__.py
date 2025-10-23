from hamcrest import assert_that, equal_to

from src.problems.leetcode.easy.build_array_from_permutation import build_array_from_permutation


def test(numbers: list[int], expected: list[int]) -> None:
    result = build_array_from_permutation(numbers)
    assert_that(result, equal_to(expected))
    print("✅", end="")


def run() -> None:
    # Example1:
    #
    # * Input: nums = [0,2,1,5,3,4]
    # * Output: [0,1,2,4,5,3]
    # * Explanation: The array ans is built as follows:
    #     ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]
    #         = [nums[0], nums[2], nums[1], nums[5], nums[3], nums[4]]
    #         = [0,1,2,4,5,3]
    test([0, 2, 1, 5, 3, 4], expected=[0, 1, 2, 4, 5, 3])

    # Example 2:
    #
    # * Input: nums = [5,0,1,2,3,4]
    # * Output: [4,5,0,1,2,3]
    # * Explanation:  The array ans is built as follows:
    #     ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]
    #         = [nums[5], nums[0], nums[1], nums[2], nums[3], nums[4]]
    #         = [4,5,0,1,2,3]
    test([5,0,1,2,3,4], expected=[4,5,0,1,2,3])


if __name__ == "__main__":
    run()
