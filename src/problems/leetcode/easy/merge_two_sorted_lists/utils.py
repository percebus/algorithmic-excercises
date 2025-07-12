from src.problems.leetcode.easy.merge_two_sorted_lists.list_node import ListNode


def list_to_nodes(numbers: list[int]) -> ListNode:
    firstListNode = ListNode()
    currentListNode = firstListNode
    for number in numbers:
        currentListNode.val = number
        currentListNode.next = ListNode()
        currentListNode = currentListNode.next

    return firstListNode


def nodes_to_list(node: ListNode) -> list[int]:
    numbers: list[int] = []
    currentNode = node
    while currentNode:
        # FIXME: Why do nodes have 0s in between?
        if currentNode.val:  # XXX?
            numbers.append(currentNode.val)

        currentNode = currentNode.next  # type: ignore[assignment]

    return numbers
