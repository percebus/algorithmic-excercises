from typing import Optional

from hamcrest import assert_that, equal_to, instance_of, is_, is_not

from problems.leetcode.easy.merge_two_sorted_lists.list_node import ListNode
from problems.leetcode.easy.merge_two_sorted_lists.utils import list_to_nodes, nodes_to_list


def test__1_2_4__gets_converted_to_and_from_nodes() -> None:
    original_list = [1, 2, 4]
    first_node: ListNode = list_to_nodes(original_list)  # type: ignore[assignment]
    assert_that(first_node, is_(instance_of(ListNode)))
    assert_that(first_node.val, equal_to(1))

    transformed_list = nodes_to_list(first_node)
    assert_that(transformed_list, equal_to([1, 2, 4]))


def test__1_3_4__gets_converted_to_and_from_nodes() -> None:
    original_list = [1, 3, 4]
    first_node: ListNode = list_to_nodes(original_list)  # type: ignore[assignment]
    assert_that(first_node, is_(instance_of(ListNode)))
    assert_that(first_node.val, equal_to(1))

    transformed_list = nodes_to_list(first_node)
    assert_that(transformed_list, equal_to([1, 3, 4]))


def test__1_1_2_3_4_4__gets_converted_to_and_from_nodes() -> None:
    original_list = [1, 1, 2, 3, 4, 4]
    first_node: ListNode = list_to_nodes(original_list)  # type: ignore[assignment]
    assert_that(first_node, is_(instance_of(ListNode)))
    assert_that(first_node.val, equal_to(1))

    transformed_list = nodes_to_list(first_node)
    assert_that(transformed_list, equal_to([1, 1, 2, 3, 4, 4]))


def test__empty__gets_converted_to_and_from_nodes() -> None:
    original_list: list[int] = []
    first_node: Optional[ListNode] = list_to_nodes(original_list)
    assert_that(first_node, is_not(instance_of(ListNode)))  # type: ignore[arg-type]
    assert_that(first_node, is_(None))  # type: ignore[misc]

    transformed_list = nodes_to_list(first_node)
    assert_that(transformed_list, equal_to([]))


def test__0__gets_converted_to_and_from_nodes() -> None:
    original_list: list[int] = [0]
    first_node: ListNode = list_to_nodes(original_list)  # type: ignore[assignment]
    assert_that(first_node, is_(instance_of(ListNode)))
    assert_that(first_node.val, equal_to(0))

    transformed_list = nodes_to_list(first_node)
    assert_that(transformed_list, equal_to([0]))
