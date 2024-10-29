from hamcrest import assert_that, equal_to, instance_of, is_
from pytest_bdd import given, parsers, scenarios, then, when

from src.problems.leetcode.easy.roman_to_integer import roman_to_int
from tests.utils import assert_is_in_range

scenarios("problems/leetcode/easy/Roman to Integer.feature")


constraints = {
    "length": {"min": 1, "max": 15},  # 1 <= s.length <= 15
    "number": {"min": 1, "max": 3999},  # It is guaranteed that s is a valid roman numeral in the range [1, 3999].
}

validate = {
    #   'string': # s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M'). # TODO
    "length": lambda numeral: assert_is_in_range(len(numeral), constraints["length"]),
    "number": lambda integer: assert_is_in_range(integer, constraints["number"]),
}


@given(parsers.parse("a roman {numeral}"), target_fixture="context")
def given_a_roman_numeral(numeral):
    validate["length"](numeral)
    return {"numeral": numeral}


@given(parsers.parse("an invalid roman {numeral}"), target_fixture="context")
def given_an_invalid_roman_numeral(numeral):
    validate["length"](numeral)
    return {"numeral": numeral}


@when("I run roman_to_int")
def when_I_run__roman_to_int(context):
    numeral = context["numeral"]
    number = None
    try:
        number = roman_to_int(numeral)
    except Exception as oException:
        context["exception"] = oException

    if number is not None:
        validate["number"](number)
        context["number"] = number

    return context


@then(parsers.parse("convert it to an {integer}"), converters={"integer": int})
def then_convert_it_to_an_integer(integer, context):
    number = context["number"]
    assert_that(number, equal_to(integer))


@then("it throws a ValueError exception")
def then_it_throws_an_exception(context):
    oException = context["exception"]
    assert_that(oException, is_(instance_of(ValueError)))
