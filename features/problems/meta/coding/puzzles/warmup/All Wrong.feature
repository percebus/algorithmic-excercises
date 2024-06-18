Feature: All Wrong

  # SRC:
  #  - https://www.facebookrecruiting.com/portal/coding_puzzles/?puzzle=1082217288848574
  #  - https://www.metacareers.com/profile/coding_puzzles/?puzzle=1082217288848574
  #
  # Constraints
  #  * 1 ≤ N ≤ 100
  #  * Ci ∈ {"A","B"}


  Scenario Outline: Matrix
    Given a multiple-choice test with <N> questions, numbered 1 to N
    And a string with <correct> answers, each labelled A and B
    When I call getWrongAnswers
    Then I get a string with the <wrong> answers

  Examples:
# |   |     answers     |
  | N | correct | wrong |
  | 1 | A       | B     |
  | 1 | B       | A     |
  | 2 | AA      | BB    |
  | 2 | AB      | BA    |
  | 2 | BA      | AB    |
  | 2 | BB      | AA    |
  | 3 | AAA     | BBB   |
  | 3 | ABA     | BAB   |
  | 3 | AAB     | BBA   |
  | 3 | ABB     | BAA   |
  | 3 | BBB     | AAA   |
  | 3 | BAB     | ABA   |
  | 3 | BAA     | ABB   |
  | 5 | BBBBB   | AAAAA |
  | 5 | AAAAA   | BBBBB |
