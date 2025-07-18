"""Google example."""

from typing import Optional

from src.problems.leetcode.easy.merge_two_sorted_lists.list_node import ListNode
from src.problems.leetcode.easy.merge_two_sorted_lists.protocol import SolutionProtocol


class Solution(SolutionProtocol):
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        tail.next = list1 or list2
        return dummy.next
