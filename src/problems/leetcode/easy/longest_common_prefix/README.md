# 14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string `""`.

```pycon
>>> from src.problems.leetcode.easy.longest_common_prefix import longest_common_prefix

```

**Example 1:**

> **Input:** `strs = ["flower","flow","flight"]`

> **Output:** `"fl"`

```pycon
>>> longest_common_prefix(["flower", "flow", "flight"])
'fl'

```

**Example 2:**

> **Input:** `strs = ["dog","racecar","car"]`

> **Output:** `""`

> **Explanation:** There is no common prefix among the input strings.

```pycon
>>> longest_common_prefix(["dog", "racecar", "car"])
''

```

**Constraints:**

- `1 <= strs.length <= 200`
- `0 <= strs[i].length <= 200`
- `strs[i]` consists of only lowercase English letters if it is non-empty.

## References

- [leetcode.com/problems/longest-common-prefix/](https://leetcode.com/problems/longest-common-prefix/description/)
