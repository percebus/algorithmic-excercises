from hamcrest import assert_that, equal_to

from src.problems.leetcode.easy.longest_common_prefix import longest_common_prefix


def test(words: list[str], expected: str) -> None:
    result = longest_common_prefix(words)
    assert_that(result, equal_to(expected))
    print("✅", end="")


def run() -> None:
    # Example1:
    #
    # * Input: strs = ["flower", "flow", "flight"]
    # * Output: "fl"
    test(["flower", "flow", "flight"], expected="fl")

    # Example 2:
    #
    # * Input: strs = ["dog", "racecar", "car"]
    # * Output: ""
    # Explanation: There is no common prefix among the input strings.
    test(["dog", "racecar", "car"], expected="")

    test([""], expected="")


if __name__ == "__main__":
    run()
