from hamcrest import assert_that, is_
from pytest_bdd import given, parsers, scenarios, then, when

from src.problems.leetcode.easy.valid_parentheses.v1 import is_valid
from tests.utils import assert_is_in_range

scenarios("problems/leetcode/easy/Valid Parentheses.feature")


constraints = {"value": {"min": 1, "max": 104}}


validate = {
    "value": lambda x: assert_is_in_range(len(x), constraints["value"]),
}


@given(
    parsers.parse("a {string} containing the characters '(', ')', '{', '}', '[' and ']'"),
    target_fixture="context",
)
def given_a_string_containing_characters(string):
    validate["value"](string)
    return {"string": string}


@when("is_valid is run")
def when__is_valid__is_run(context):
    string = context["string"]
    context["result"] = is_valid(string)


@then("determine that the input string is valid")
def then_determine_that_input_string_is_valid(context):
    result = context["result"]
    assert_that(result, is_(True))


@then("determine that the input string is NOT valid")
def then_determine_that_input_string_is_not_valid(context):
    result = context["result"]
    assert_that(result, is_(False))
