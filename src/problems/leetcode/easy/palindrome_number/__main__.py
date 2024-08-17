from hamcrest import assert_that, equal_to

from src.problems.leetcode.easy.palindrome_number.v1 import is_palindrome

# SRC: https://leetcode.com/problems/palindrome-number/
#
# Given an integer x, return true if x is palindrome integer.
# An integer is a palindrome when it reads the same backward as forward.
# For example, 121 is a palindrome while 123 is not.


def test(number: int, expected: bool):
    result = is_palindrome(number)
    #   print(f'{number}: {result}') # DEBUG only
    assert_that(result, equal_to(expected))
    print("✅", end="")


def run():
    # Input: x = 121
    # Output: true
    # Explanation: 121 reads as 121 from left to right and from right to left.
    test(121, expected=True)

    test(123, expected=False)

    test(1221, expected=True)

    # Input: x = -121
    # Output: false
    # Explanation: From left to right, it reads -121. From right to left, it becomes 121-.
    # Therefore it is not a palindrome.
    test(-121, expected=False)

    # Input: x = 10
    # Output: false
    # Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
    test(10, expected=False)


if __name__ == "__main__":
    run()
