Feature: Largest Palindrome Product
  # A palindromic number reads the same both ways.
  # The largest palindrome made from the product of two `2`-digit numbers is `9009 = 91 x 99`.
  # Find the largest palindrome made from the product of two `3`-digit numbers.

  Scenario Outline: 2 & 3 digit numbers
    Given 2 <digits>-digit numbers
    When I run get_largest_paindrome_product
    Then I get <factor1> and <factor2> factors
    And its <product> is the largest palindrome

  Examples:
  | digits | factor1 | x | factor2 | = | product |
  |      2 |      91 | x |      99 | = |    9009 |
  |      3 |     913 | x |     993 | = |  906609 |
