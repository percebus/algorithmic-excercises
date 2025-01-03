from typing import Optional

from hamcrest import assert_that, equal_to

from src.problems.leetcode.easy.reverse_string import reverse_string


def test(chars: list[str], expected: Optional[list[str]] = None) -> None:
    reverse_string(chars)
    actual_string: str = "".join(chars)
    expected_string: str = "".join(expected or [])
    assert_that(actual_string, equal_to(expected_string))
    print("✅", end="")


def run() -> None:
    # Example 1:
    # Input: s = ['h','e','l','l','o']
    # Output: ['o','l','l','e','h']
    test(["h", "e", "l", "l", "o"], expected=["o", "l", "l", "e", "h"])

    # Example 2:
    # Input: s = ['H', 'a', 'n', 'n', 'a', 'h']
    # Output: ['h', 'a', 'n', 'n', 'a', 'H']
    test(["H", "a", "n", "n", "a", "h"], expected=["h", "a", "n", "n", "a", "H"])

    print("\n")


if __name__ == "__main__":
    run()
