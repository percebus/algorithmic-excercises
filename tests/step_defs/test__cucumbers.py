from hamcrest import assert_that, equal_to
from pytest_bdd import given, parsers, scenarios, then, when

scenarios("Eat cucumbers.feature")


@given(parsers.parse("there are {start:d} cucumbers"), target_fixture="cucumbers")
def given_cucumbers(start):
    return {"start": start, "eat": 0}


@when(parsers.parse("I eat {eat:d} cucumbers"))
def eat_cucumbers(cucumbers, eat):
    cucumbers["eat"] += eat


@then(parsers.parse("I should have {left:d} cucumbers"))
def should_have_left_cucumbers(cucumbers, left):
    assert_that(cucumbers["start"] - cucumbers["eat"], equal_to(left))
