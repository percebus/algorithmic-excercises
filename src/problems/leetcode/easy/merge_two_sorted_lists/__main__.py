from typing import Optional
from hamcrest import assert_that, equal_to

from src.problems.leetcode.easy.merge_two_sorted_lists.list_node import ListNode
from src.problems.leetcode.easy.merge_two_sorted_lists.utils import list_to_nodes, nodes_to_list

from src.problems.leetcode.easy.merge_two_sorted_lists import merge_two_sorted_lists


def test(list1: list[int], list2: list[int], expected: list[int]) -> None:
    node1: ListNode = list_to_nodes(list1)
    node2: ListNode = list_to_nodes(list2)
    last_node: Optional[ListNode] = merge_two_sorted_lists(node1, node2)
    if last_node is None:
        raise ValueError("What happened?")

    result = nodes_to_list(last_node)

    assert_that(result, equal_to(expected))
    print("✅", end="")


def run() -> None:
    # Example1:
    #
    # * Input: list1 = [1,2,4], list2 = [1,3,4]
    # * Output: [1,1,2,3,4,4]
    test([1, 2, 4], [1, 3, 4], expected=[1, 1, 2, 3, 4, 4])


if __name__ == "__main__":
    run()
