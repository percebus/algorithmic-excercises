Feature: Reverse String

  # SRC: https://leetcode.com/problems/reverse-string/

  # Constraints
  # - 1 <= s.length <= 105
  # - s[i] is a printable ascii character.


  Scenario Outline: _
    Given an array of <chars>
    When I call reverseString
    Then the void function returns None
    And the same array is procedurally <reversed> by reference

  Examples:
  |    chars    |  reversed   |
  |   h,e,l,l,o | o,l,l,e,h   |
  | H,a,n,n,a,h | h,a,n,n,a,H |
