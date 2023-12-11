Feature: Two Sum

  # SRC: https://leetcode.com/problems/two-sum/
  #
  # Constraints:
  #   * 2 <= nums.length <= 104
  #   * -109 <= nums[i] <= 109
  #   * -109 <= target <= 109
  #   * Only one valid answer exists. # TODO TEST

  Scenario Outline: Arrays
    Given an array of integer <numbers>
    And an integer <target> number
    When two_sum is invoked
    Then it returns <indexes> of the <two_numbers>
    And they add up to <target>

    Examples:
    |  case   |    numbers     | target | indexes | two_numbers |
    |         | [2, 7, 11, 15] |      9 | [0, 1]  |   [2, 7]    |
    |         | [3, 2, 4]      |      6 | [1, 2]  |   [2, 4]    |
    | 3 x2    | [3, 3]         |      6 | [0, 1]  |   [3, 3]    |
  # | 60 + 70 | [60, 70]       |    110 | [0, 1]  |  [60, 70]   | # Negative test: target.- outside constraints
  # | 110 x2  | [110, 110]     |    240 | [0, 1]  | [110, 110]  | # Negative test: value.-  outside constraints


  Scenario Outline: Ranges
    Given an array of integer <numbers>
    And an integer <target> number
    When two_sum is invoked
    Then it returns <indexes> of the <two_numbers>
    And they add up to <target>

    Examples:
      |   case |   numbers    | target | indexes  | two_numbers |
      | 0-13   | range(14)    |     13 |  [0, 13] |   [0, 13]   |
      | 1-13   | range(1, 14) |     13 |  [0, 11] |   [1, 12]   |
      | 0-99   | range(100)   |     13 |  [0, 13] |   [0, 13]   |
    # | 0-200  | range(201)   |     13 |  [0, 13] |   [0, 13]   | # Negative test: length.- outside constraints
