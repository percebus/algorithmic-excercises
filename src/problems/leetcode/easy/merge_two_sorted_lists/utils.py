

from src.problems.leetcode.easy.merge_two_sorted_lists.list_node import ListNode


def list_to_nodes(numbers: list[int]) -> ListNode:

    firstListNode = ListNode()
    currentListNode = firstListNode
    for number in numbers:
        currentListNode.val = number
        currentListNode.next = ListNode()
        currentListNode = currentListNode.next

    return firstListNode


def nodes_to_list(node: ListNode):

    numbers: list[int] = []
    currentNode = node
    while currentNode:
        # XXX?
        if currentNode.val:
            numbers.append(currentNode.val)
        currentNode = currentNode.next

    return numbers
