Feature: Merge Two Sorted Arrays

  # SRC: https://leetcode.com/problems/merge-two-sorted-arrays/
  #
  # Constraints:
  # - The number of nodes in both lists is in the range [0, 50].
  # - -100 <= Node.val <= 100
  # - Both list1 and list2 are sorted in non-decreasing order.

Scenario Outline: Both ListNodes have values
    Given the heads of two sorted linked lists <list1> and <list2>
    When merge_sorted_arrays is invoked
    Then it merges the two lists into one sorted list <result>
    And it returns the <head> of the merged linked list

  Examples:
    |     list1     |     list2     |       result                 | head |
    | (1)->(2)->(4) | (1)->(3)->(4) | (1)->(1)->(2)->(3)->(4)->(4) | (1)  |


Scenario Outline: Some ListNodes are None
    Given the heads of two sorted linked lists <list1> and <list2>
    When merge_sorted_arrays is invoked
    Then it merges the two lists into one sorted list <result>
    And it returns the <head> of the merged linked list

  Examples:
    | list1 | list2 | result | head |
    | None  | (0)   | (0)    | (0)  |

Scenario Outline: Both ListNodes are None
    Given the heads of two sorted linked lists <list1> and <list2>
    When merge_sorted_arrays is invoked
    Then it merges the two lists into one sorted list <result>
    And it returns the <head> of the merged linked list
    | list1 | list2 | result | head |
    | None  | None  | None   | None |
