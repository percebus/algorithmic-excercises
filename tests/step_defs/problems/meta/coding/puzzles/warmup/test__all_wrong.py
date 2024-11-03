from typing import Any

from hamcrest import assert_that, equal_to
from pytest_bdd import given, parsers, scenarios, then, when

from src.problems.meta.coding.puzzles.warmup.all_wrong import get_wrong_answers

scenarios("problems/meta/coding/puzzles/warmup/All Wrong.feature")


@given(parsers.parse("a multiple-choice test with {N} questions, numbered 1 to N"), converters={"N": int}, target_fixture="context")
def given_a_test_with_N_questions(N: int) -> dict[str, Any]:
    return {"N": N}


@given(parsers.parse("a string with {correct} answers, each labelled A and B"))
def given_a__string_with_correct_answers(correct: str, context: dict[str, Any]) -> dict[str, Any]:
    context["correct_answers"] = correct
    return context


@when("I call getWrongAnswers")
def when_i_call_getWrongAnswers(context: dict[str, Any]) -> dict[str, Any]:
    N = context["N"]
    correct_answers = context["correct_answers"]
    result = get_wrong_answers(N, correct_answers)
    context["result"] = result
    return context


@then(parsers.parse("I get a string with the {wrong} answers"))
def then_i_get_a_string_with_wrong_answers(wrong: str, context: dict[str, Any]) -> None:
    expected = wrong
    actual = context["result"]
    assert_that(actual, equal_to(expected))
