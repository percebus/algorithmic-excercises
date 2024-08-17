from typing import Any

from hamcrest import assert_that, equal_to
from pytest_bdd import given, parsers, scenarios, then, when

from src.problems.euler.multiples_of_3_or_5.v2 import sum_multiples

scenarios("problems/euler/Sum Multiples of 3 or 5.feature")


def parse_multiples(string: str) -> list[int]:
    strings = string.split(", ")
    ints = map(int, strings)
    return list(ints)


@given(parsers.parse("a {limit} number"), converters={"limit": int}, target_fixture="context")
def given_a_limit_number(limit: int):
    return {"limit": limit}


@given(parsers.parse("a few {multiples} to divide by"), converters={"multiples": parse_multiples})
def given_a_few_multiples(multiples: list[int], context: dict[str, Any]):
    context["multiples"] = multiples
    return context


@when("I call sum_multiples")
def when_I_call__sum_multiples(context: dict[str, Any]):
    limit = context["limit"]
    multiples = context["multiples"]
    result = sum_multiples(limit, multiples)
    context["result"] = result
    return context


@then(parsers.parse("I get the expected {result}"), converters={"result": int})
def step_impl(result: int, context: dict[str, Any]):
    expected = int(result)
    actual = context["result"]
    assert_that(expected, equal_to(actual))
