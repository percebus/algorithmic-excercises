# SRC: https://leetcode.com/problems/longest-common-prefix/
#
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string.


def longest_common_prefix(words: list[str]) -> str:
    """Longest Common Prefix

    Args:
        words (list[str]): Different words that might share a common prefix.

    Returns:
        str: A prefix that is common to all words in the list.
    """

    first_word: str = words[0]
    chars: list[str] = list(first_word)
    prefix: str = ""
    result: str = prefix
    for char in chars:
        prefix += char
        invalid = next((word for word in words if not word.startswith(prefix)), None)
        if invalid is None:
            result = prefix
        else:
            return result

    return result
