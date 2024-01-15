# SRC: https://leetcode.com/problems/longest-common-prefix/


# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
from hamcrest import assert_that, equal_to


def longest_common_prefix(words):
    first_word = words[0]
    chars = list(first_word)
    prefix = ""
    result = prefix
    for char in chars:
        prefix += char
        invalid = next((word for word in words if not word.startswith(prefix)), None)
        if invalid is None:
            result = prefix
        else:
            return result
    return result


def test(words, expected=None):
    result = longest_common_prefix(words)
    assert_that(result, equal_to(expected))
    print("✅", end="")


def run():
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

    print("\n")


if __name__ == "__main__":
    run()
