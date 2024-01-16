from typing import Optional

from hamcrest import assert_that, equal_to

brackets = {"[": "]", "{": "}", "(": ")"}


"""
SRC: https://leetcode.com/problems/valid-parentheses/

An input string is valid if:
 * Open brackets must be closed by the same type of brackets.
 * Open brackets must be closed in the correct order.
"""


def is_valid(string: str) -> bool:
    opened: list[str] = []  # TODO? use queue instead?
    for char in string:
        # pylint: disable=consider-iterating-dictionary
        is_opening: bool = char in brackets.keys()
        is_closing: bool = char in brackets.values()
        # pylint: enable=consider-iterating-dictionary

        if is_opening:
            opened.append(char)
        elif is_closing:
            last_opened: Optional[str] = opened[-1] if opened else None
            if char == brackets.get(last_opened):  # type: ignore
                opened.pop()
            else:
                return False
        else:
            pass  # any other char

    return not opened


def test(string, expected=None) -> None:
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

    print("\n")


if __name__ == "__main__":
    run()
