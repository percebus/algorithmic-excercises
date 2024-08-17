from hamcrest import assert_that, equal_to

from src.problems.leetcode.easy.valid_parentheses.v1 import is_valid


def test(string: str, expected: bool) -> None:
    result = is_valid(string)
    assert_that(result, equal_to(expected))
    print("✅", end="")


def run():
    # Example 1:
    #  * Input: s = "()"
    #  * Output: true
    test("()", expected=True)

    # Example 2:
    #  * Input: s = "()[]{}"
    #  * Output: true
    test("()[]{}", expected=True)

    # Example 3:
    #  * Input: s = "(]"
    #  * Output: false
    test("(]", expected=False)

    # Example
    #  * Input: s = "["
    #  * Output: false
    test("[", expected=False)


if __name__ == "__main__":
    run()
