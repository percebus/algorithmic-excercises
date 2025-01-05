Feature: Reverse String

  # SRC: https://leetcode.com/problems/reverse-string/

  # Constraints
  # - 1 <= s.length <= 105
  # - s[i] is a printable ascii character.


  Scenario Outline: Even-sized words
    Given an array of <chars>
    When I call reverseString
    Then the void function returns None
    And the same array is procedurally <reversed> by reference
#   And it used 0(1) extra memory # TODO how to test?

  Examples:
  |    chars    |  reversed   | size |
  | H,a,n,n,a,h | h,a,n,n,a,H |    6 |


  Scenario Outline: Odd-sized words
    Given an array of <chars>
    When I call reverseString
    Then the void function returns None
    And the same array is procedurally <reversed> by reference
#   And it used 0(1) extra memory # TODO how to test?

  Examples:
  |  chars    |  reversed | size |
  | h,e,l,l,o | o,l,l,e,h |    5 |
