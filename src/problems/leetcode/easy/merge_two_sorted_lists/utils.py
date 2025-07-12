from typing import Optional

from src.problems.leetcode.easy.merge_two_sorted_lists.list_node import ListNode


def list_to_nodes(numbers: list[int]) -> Optional[ListNode]:
    firstListNode = ListNode()
    currentListNode = firstListNode
    for number in numbers:
        currentListNode.next = ListNode()
        currentListNode = currentListNode.next
        currentListNode.val = number

    return firstListNode.next


def nodes_to_list(node: Optional[ListNode]) -> list[int]:
    numbers: list[int] = []
    currentNode = node
    while currentNode:
        numbers.append(currentNode.val)
        currentNode = currentNode.next

    return numbers
