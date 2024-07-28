from hamcrest import assert_that, instance_of, is_
from pytest_bdd import given, parsers, scenarios, then, when

from src.problems.leetcode.easy.palindrome_number.v1 import is_palindrome
from tests.utils import assert_is_in_range

constraints = {
    "value": {  # -2^31 <= x <= 2^31 -1
        "min": -(2**31),
        "max": (2**31) - 1,
    }
}

validate = {"value": lambda x: assert_is_in_range(x, constraints["value"])}


scenarios("problems/leetcode/easy/Palindrome Number.feature")


@given(parsers.parse("an integer number {number}"), converters={"number": eval}, target_fixture="context")
def given_a_valid_number(number):
    validate["value"](number)
    return {"number": number}


@given(parsers.parse("an invalid integer number {number}"), converters={"number": eval}, target_fixture="context")
def given_an_invalid_number(number):
    try:
        validate["value"](number)
        return {"number": number}
    except Exception as exception:
        return {"exception": exception}


@when("is_palindrome is invoked")
def when__is_palindrome__is_invoked(context):
    number = context["number"]
    context["result"] = is_palindrome(number)
    return context


@then("return True if x is palindrome integer")
def then_returns_True_if_number_is_palindrome(context):
    result = context["result"]
    assert result is True


@then("return False if x is NOT palindrome integer")
def then_returns_False_if_number_is_not_palindrome(context):
    result = context["result"]
    assert result is False


@then("handle the exception for the very large number")
def then_it_handles_the_exception_for_very_large_number(context):
    exception = context["exception"]
    assert_that(exception, is_(instance_of(Exception)))
