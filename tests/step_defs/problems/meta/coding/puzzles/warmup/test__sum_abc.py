from hamcrest import assert_that, equal_to
from pytest_bdd import given, parsers, scenarios, then, when

from src.problems.meta.coding.puzzles.warmup.sum_abc import getSum

scenarios("problems/meta/coding/puzzles/warmup/sum ABCs.feature")


@given(parsers.parse("three integers {A}, {B}, and {C}"), converters={"A": int, "B": int, "C": int}, target_fixture="context")
def given_3_integers(A, B, C):
    # TODO validate restrictions
    return {"A": A, "B": B, "C": C}


@when("I call getSum")
def when_I_call_getSyum(context):
    A = context["A"]
    B = context["B"]
    C = context["C"]
    result = getSum(A, B, C)
    context["result"] = result
    return context


@then(parsers.parse("it determines their {result}"), converters={"result": int})
def then_it_determines_their_result(result, context):
    expected_result = result
    actual_result = context["result"]
    assert_that(expected_result, equal_to(actual_result))
