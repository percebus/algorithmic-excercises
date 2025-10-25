from typing import Any, Optional

from hamcrest import assert_that, equal_to, is_
from pytest_bdd import given, parsers, scenarios, then, when

from problems.leetcode.easy.merge_two_sorted_lists import merge_two_sorted_lists
from problems.leetcode.easy.merge_two_sorted_lists.list_node import ListNode


def extract_numbers(text: str) -> list[int]:
    """Extracts numbers from the string representation of a list of nodes."""
    str_numbers = text.replace("(", "").replace(")", "").split("->")

    int_numbers = map(int, str_numbers)
    return list(int_numbers)


def build_linked_list(numbers: list[int]) -> ListNode:
    """Builds a linked list from a list of numbers."""
    first_number: int = numbers[0]
    headListNode = ListNode(first_number)
    currentListNode = headListNode

    for number in numbers[1:]:
        currentListNode.next = ListNode(number)
        currentListNode = currentListNode.next

    return headListNode


def parse_linked_list(string: str) -> Optional[ListNode]:
    """Parses a string representation of a linked list into a ListNode."""
    if string == "None":
        return None

    numbers = extract_numbers(string)
    return build_linked_list(numbers)


def extract_linked_list_values(head: Optional[ListNode]) -> list[int]:
    """Extracts values from a linked list into a list of integers."""
    values: list[int] = []
    current = head
    while current is not None:
        values.append(current.val)
        current = current.next

    return values


scenarios("problems/leetcode/easy/Merge Two Sorted Lists.feature")


@given(
    parsers.parse("the heads of two sorted linked lists {list1} and {list2}"),
    converters={"list1": parse_linked_list, "list2": parse_linked_list},
    target_fixture="context",
)
def given_the_heads_of_two_sorted_linked_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> dict[str, Any]:
    return {"list1": list1, "list2": list2}


@when("merge_sorted_arrays is invoked")
def when_merge_sorted_arrays_is_invoked(context: dict[str, Any]) -> None:
    aListNode: Optional[ListNode] = context["list1"]
    anotherListNode: Optional[ListNode] = context["list2"]
    resultingListNode: Optional[ListNode] = merge_two_sorted_lists(aListNode, anotherListNode)
    context["result"] = resultingListNode


@then(
    parsers.parse("it returns the {head} of the merged linked list"),
    converters={"head": parse_linked_list},
)
def then_it_returns_the_head_of_the_merged_linked_list(context: dict[str, Any], head: Optional[ListNode]) -> None:
    result: Optional[ListNode] = context["result"]
    if head is None:
        assert_that(result, is_(None))
    else:
        resultingListNode: ListNode = result  # type: ignore
        assert_that(resultingListNode.val, equal_to(head.val))


@then(
    parsers.parse("it merges the two lists into one sorted list {result}"),
    converters={"result": parse_linked_list},
)
def then_it_merges_the_two_lists_into_one_sorted_list(context: dict[str, Any], actualListNode: Optional[ListNode]) -> None:
    actualListNode: Optional[ListNode] = context["result"]
    expectedListNode: Optional[ListNode] = parse_linked_list(actualListNode)
    assert_that(actualListNode, equal_to(expectedListNode))
    if expectedListNode is None:
        assert_that(actualListNode, is_(None))
    else:
        actual_values: list[int] = extract_linked_list_values(actualListNode)
        expected_values: list[int] = extract_linked_list_values(expectedListNode)

        assert_that(actual_values, equal_to(expected_values))
