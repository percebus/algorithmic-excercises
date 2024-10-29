from typing import Optional

from hamcrest import assert_that, equal_to

from src.problems.interviews.shortest_common_prefixes import get_prefixes


def test(words: list[str], expected: Optional[list[str]] = None):
    actual = get_prefixes(words)
    assert_that(expected, equal_to(actual))
    print("✅", end="")


def run():
    test([], expected=[])
    test(["dog", "zebra", "bananas"], expected=["b", "d", "z"])
    test(["dog", "zebra", "duck", "bananas"], expected=["b", "do", "du", "z"])
    test(["dog", "zebra", "duck", "dove", "bananas"], expected=["b", "dog", "dov", "du", "z"])


if __name__ == "__main__":
    run()
