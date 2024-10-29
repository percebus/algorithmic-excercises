from typing import Any

from hamcrest import assert_that, equal_to
from pytest_bdd import parsers


# FIXME
def _test__parse__two_sum__given() -> None:
    oParse = parsers.parse("an {array} of integer numbers")
    result: dict[str, Any] = oParse.parse_arguments("[2, 7, 11, 15]")
    expected: str = "an [2, 7, 11, 15] of integer numbers"
    assert_that(result, equal_to(expected))


def test_format() -> None:
    array_string: str = "[2, 7, 11, 15]"
    actual_string: str = "an {array} of integer numbers".format(array=array_string)
    expected_string: str = "an [2, 7, 11, 15] of integer numbers"
    assert_that(actual_string, equal_to(expected_string))

    actual_array: list[int] = eval(array_string)
    expected_array: list[int] = [2, 7, 11, 15]
    assert_that(actual_array, equal_to(expected_array))
