Feature: Largest Palindrome Product
  # The prime factors of 13,195 are 5, 7, 13 and 29.
  # What is the largest prime factor of the number 600,851,475,143?

  Scenario Outline: ProjectEuler.net
    Given 1 number <number>
    When I run get_largest_prime_factor
    Then I get the expected number <result>

  Examples:
  |    number    | result | prime_factors |
  |        13195 |     29 |  5, 7, 13, 29 |
  | 600851475143 |   6857 |     ???       |


  Scenario Outline: grae.io
    Given 1 number <number>
    When I run get_largest_prime_factor
    Then I get the expected number <result>

  Examples:
  | number | result | prime_factors |
  |  21952 |     7  |     ???       |
  |  98989 |   8999 |     ???       |
