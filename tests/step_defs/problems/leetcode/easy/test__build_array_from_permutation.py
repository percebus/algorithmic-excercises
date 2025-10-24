from typing import Any

from hamcrest import assert_that, equal_to
from pytest_bdd import given, parsers, scenarios, then, when

from src.problems.leetcode.easy.build_array_from_permutation import build_array_from_permutation

scenarios("problems/leetcode/easy/Build Array from Permutation.feature")


ContextType = dict[str, Any]


@given(parsers.parse("a zero-based permutation {nums} array (0-indexed)"), converters={"nums": eval}, target_fixture="context")
def given_a_zero_based_permutation(nums: list[int]) -> ContextType:
    return {"nums": nums}


@when("build_array_from_permutation is invoked")
def when__build_array_from_permutation__is_invoked(context: ContextType) -> ContextType:
    nums = context["nums"]
    context["ans"] = build_array_from_permutation(nums)
    return context


@then(
    parsers.parse("it returns an array {ans}wer"),
    converters={"ans": eval},
)
def then_it_returns_an_array(context: ContextType, ans: list[int]) -> None:
    actual_answer = context["ans"]
    expected_answer = ans
    assert_that(actual_answer, equal_to(expected_answer))
