from io import StringIO

import pandas
from hamcrest import assert_that, equal_to
from pytest_bdd import given, parsers, scenarios, then, when

from src.problems.meta.coding.puzzles.warmup.battleship import getHitProbability

scenarios("problems/meta/coding/puzzles/warmup/Battleship.feature")


@given("a battleship matrix of 2 by 3")
def given_a_battleship_matrix_of_2_by_3(
    target_fixture="context",
):
    return {"R": 2, "C": 3}


@given("a battleship matrix of 2 by 2")
def given_a_battleship_matrix_of_2_by_2(
    target_fixture="context",
):
    return {"R": 2, "C": 2}


@given(parsers.parse("with the following data:\n{data}"))
def given_with_the_following_data(data, target_fixture="context"):
    oStringIO = StringIO(data)
    oDataFrame = pandas.read_csv(oStringIO, header=None, sep="|")
    grid = oDataFrame.values.tolist()
    return {"grid": grid}


@when("I call getHitProbability")
def when_I_call_getHitProbability(context):
    R = context["R"]
    C = context["C"]
    grid = context["grid"]
    context["result"] = getHitProbability(R, C, grid)
    return context


@then(parsers.parse("it returns a hit probability of {percent}%"))
def then_it_returns_a_hit_probability_of_50(percent, context):
    result = context["result"]
    assert_that(result, equal_to(percent))
