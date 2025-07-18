"""v1 implementation."""

from typing import Optional

from src.problems.leetcode.easy.merge_two_sorted_lists.list_node import ListNode
from src.problems.leetcode.easy.merge_two_sorted_lists.protocol import SolutionProtocol


class Solution(SolutionProtocol):
    """Solution class."""

    # Time Complexity: O(M+N)
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        v1.Solution.mergeTwoLists.

        Args:
            list1 (Optional[ListNode]): First node of Red list
            list2 (Optional[ListNode]): First node of Purple list

        Returns
        -------
            Optional[ListNode]: First Node
        """
        firstListNode = ListNode()

        # By ref
        lastListNode = firstListNode

        # We don't want to re-assing list1 or list2
        redListNode = list1
        purpleListNode = list2
        while redListNode and purpleListNode:
            if redListNode.val < purpleListNode.val:
                # Assign tail to the lower value
                lastListNode.next = redListNode

                # Shift red to next node
                redListNode = redListNode.next
            else:
                # Assign tail to the lower value
                lastListNode.next = purpleListNode

                # Shift purple to next node
                purpleListNode = purpleListNode.next

            # Since the 2 lists are pre-sorted
            # We point to the next node
            lastListNode = lastListNode.next

        # Since we ran out of values
        # We point to w/e is remaining
        lastListNode.next = redListNode or purpleListNode

        # Since firstListNode doesn't contain a value in itself
        # We'll return the next one.
        return firstListNode.next


solution = Solution()
