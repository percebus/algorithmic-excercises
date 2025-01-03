from hamcrest import assert_that, equal_to, is_
from pytest_bdd import given, parsers, scenarios, then, when

from src.problems.leetcode.easy.reverse_string import reverse_string

scenarios("problems/leetcode/easy/Reverse String.feature")


@given(parsers.parse("an array of {chars}"), target_fixture="context")
def given_an_array_of_chars(chars):
    return {"chars": chars}


@when("I call reverseString")
def when_I_call_reverseString(context):
    chars = context["chars"]
    copy = list(chars)
    context["result"] = reverse_string(copy)
    context["reeversed"] = copy


@then("the void function returns None")
def then_it_returns_None(context):
    result = context["result"]
    assert_that(result, is_(None))


@then(parsers.parse("the same array is procedurally {expected_reversed} by reference"))
def then_the_string_got_reversed(expected_reversed, context):
    reversed = context["reversed"]
    reversed_chars = reversed.split(",")

    assert_that(expected_reversed, equal_to(reversed_chars))
