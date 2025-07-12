from typing import TYPE_CHECKING, Optional

from hamcrest import assert_that, equal_to

from src.problems.leetcode.easy.merge_two_sorted_lists import merge_two_sorted_lists
from src.problems.leetcode.easy.merge_two_sorted_lists.utils import list_to_nodes, nodes_to_list

if TYPE_CHECKING:
    from src.problems.leetcode.easy.merge_two_sorted_lists.list_node import ListNode


def test(list1: list[int], list2: list[int], expected: list[int]) -> None:
    first_node1: Optional[ListNode] = list_to_nodes(list1)
    first_node2: Optional[ListNode] = list_to_nodes(list2)
    first_merged_node: Optional[ListNode] = merge_two_sorted_lists(first_node1, first_node2)
    result = nodes_to_list(first_merged_node)

    assert_that(result, equal_to(expected))
    print("✅", end="")


def run() -> None:
    # Example1:
    #
    # - Input: list1 = [1,2,4], list2 = [1,3,4]
    # - Output: [1,1,2,3,4,4]
    test([1, 2, 4], [1, 3, 4], expected=[1, 1, 2, 3, 4, 4])

    # Example 2:
    #
    # - Input: list1 = [], list2 = []
    # - Output: []
    test([], [], expected=[])

    # Example 3:
    #
    # - Input: list1 = [], list2 = [0]
    # - Output: [0]
    test([], [0], expected=[0])


if __name__ == "__main__":
    run()
