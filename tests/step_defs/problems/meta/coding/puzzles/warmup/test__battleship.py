from io import StringIO

import numpy
import pandas
from hamcrest import assert_that, equal_to
from pytest_bdd import given, parsers, scenarios, then, when

from src.problems.meta.coding.puzzles.warmup.battleship.v1 import getHitProbability

scenarios("problems/meta/coding/puzzles/warmup/Battleship.feature")


@given(parsers.parse("a battleship matrix of {x} by {y}"), converters={"x": int, "y": int}, target_fixture="context")
def given_a_battleship_matrix_of_x_by_y(x, y):
    return {"R": x, "C": y}


@given(parsers.parse("with the following data:\n{data}"))
def given_with_the_following_data(data, context):
    oStringIO = StringIO(data)
    oDataFrame = pandas.read_csv(oStringIO, header=None, sep="|")
    lists = oDataFrame.values.tolist()
    clean_lists = [filter(lambda number: (not numpy.isnan(number)), numbers) for numbers in lists]
    context["grid"] = [list(numbers) for numbers in clean_lists]
    return context


@when("I call getHitProbability")
def when_I_call_getHitProbability(context):
    R = context["R"]
    C = context["C"]
    grid = context["grid"]
    context["result"] = getHitProbability(R, C, grid)
    return context


@then(parsers.parse("it returns a hit probability of {percent}%"), converters={"percent": float})
def then_it_returns_a_hit_probability_of_x_percent(percent, context):
    result = context["result"]
    actual = result * 100
    assert_that(actual, equal_to(percent))
