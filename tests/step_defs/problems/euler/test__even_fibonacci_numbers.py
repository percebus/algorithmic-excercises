from hamcrest import assert_that, equal_to
from pytest_bdd import given, parsers, scenarios, then, when

from src.problems.euler.even_fibonacci_numbers import sum_fibonacci_evens

scenarios("problems/euler/Sum Even Fibonacci Numbers.feature")


@given(parsers.parse("a {limit} number"), converters={"limit": int}, target_fixture="context")
def given_a_limit_number(limit):
    return {"limit": limit}


@when("I call sum_evens")
def when_I_call_sub_fibonacci_evens(context):
    result = sum_fibonacci_evens(context["limit"])
    context["result"] = result
    return context


@then(parsers.parse("I get the {total} sum of all even numbers inside the Fibonacci series, up until that limit"), converters={"total": int})
def then_I_get_the_total_sum(total, context):
    result = context["result"]
    assert_that(total, equal_to(result))
