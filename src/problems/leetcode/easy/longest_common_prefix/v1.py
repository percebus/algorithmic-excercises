from problems.leetcode.easy.longest_common_prefix.base import SolutionInterface


class Solution(SolutionInterface):
    def longestCommonPrefix(self, words: list[str]) -> str:
        """Solution.longestCommonPrefix.

        Calculate the Longest Common Prefix.

        Parameters
        ----------
            - `words:list[str]`.- Different words that might share a common prefix.

        Returns
        -------
            - :result: str:
              - The longest common prefix string amongst an array of strings.
              - If there is no common prefix, it returns an empty string.

        Examples
        --------
        >>> solution = Solution()
        >>> solution.longestCommonPrefix(["flower", "flow", "flight"])
        'fl'

        >>> solution.longestCommonPrefix(["dog", "racecar", "car"])
        ''
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


solution = Solution()
