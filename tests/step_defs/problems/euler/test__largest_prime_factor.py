from typing import Any, Optional

from hamcrest import assert_that, equal_to
from pytest_bdd import given, parsers, scenarios, then, when

from problems.euler.largest_prime_factor import get_largest_prime_factor

scenarios("problems/euler/Largest Prime Factor.feature")


@given(parsers.parse("1 number {number}"), converters={"number": int}, target_fixture="context")
def given_a_limit_number(number: int) -> dict[str, Any]:
    return {"number": number}


@when("I run get_largest_prime_factor")
def when_I_run__get_largest_prime_factor(context: dict[str, Any]) -> dict[str, Any]:
    number: int = context["number"]
    result: Optional[int] = get_largest_prime_factor(number)
    context["result"] = result
    return context


@then(parsers.parse("I get the expected number {result}"), converters={"result": int})
def then_I_get_result(result: int, context: dict[str, Any]) -> None:
    actual_result: int = context["result"]
    assert_that(actual_result, equal_to(result))
