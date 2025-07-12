from typing import Optional, Protocol, runtime_checkable

from src.problems.leetcode.easy.merge_two_sorted_lists.list_node import ListNode

"""
SRC: https://leetcode.com/problems/merge-two-sorted-lists/

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""


@runtime_checkable  # NOTE: Allows for isinstance check.
class SolutionProtocol(Protocol):
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """Merge Two Sorted Lists.

        Args:
            list1 (Optional[ListNode]): First node of Red list
            list2 (Optional[ListNode]): First node of Purple list

        Returns
        -------
            Optional[ListNode]: First Node
        """
