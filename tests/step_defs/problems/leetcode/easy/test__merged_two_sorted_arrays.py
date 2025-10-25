

from problems.leetcode.easy.merge_two_sorted_lists.list_node import ListNode


def clean_nodes(string: str) -> str:
    """Cleans the string representation of a list of nodes by removing 'Node' substrings."""
    return string\
        .replace("(", "")\
        .replace(")", "")

def extract_numbers(string: str) -> list[int]:
    """Extracts numbers from the string representation of a list of nodes."""
    return [
        int(num)
        for num in string.split("->")
    ]

def build_linked_list(numbers: list[int]) -> ListNode | None:
    """Builds a linked list from a list of numbers."""
    headListNode = ListNode(numbers[0])
    currentListNode = headListNode

    for number in numbers[1:]:
        currentListNode.next = ListNode(number)
        currentListNode = currentListNode.next

    return headListNode
