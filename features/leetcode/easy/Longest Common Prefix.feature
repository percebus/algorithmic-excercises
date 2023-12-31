Feature: Longest Common Prefix

  # SRC: https://leetcode.com/problems/longest-common-prefix/
  #
  # Constraints:
  #  * 1 <= strs.length <= 200
  #  * 0 <= strs[i].length <= 200
  #  * strs[i] consists of only lower-case English letters.


  Scenario Outline: Common prefix
    Given some <words>
    When longest_common_prefix is invoked
    Then it finds the longest common <prefix> string amongst an array of strings

  Examples:
  |       words          | prefix |
  | flower, flow, flight | fl     |
  | dog, dove            | do     |
  | dog, dove, duck      | d      |
  | dog, duck            | d      |
  | dove, duck           | d      |
  | ''                   | ''     |


  Scenario Outline: No common prefix
    Given some <words>
    When longest_common_prefix is invoked
    Then it returns an empty string

  Examples:
  |         words          |
  | ''                     |
  | flower, ''             |
  | dog, racecar, car      |
  | dog, dove, duck, zebra |


  Scenario Outline: Out of bounds
    Given an array of invalid <strings>
    Then it handles the exception for the invalid chars

  Examples:
  |   strings  |
  | !          |
  | !, @, #, ? |
