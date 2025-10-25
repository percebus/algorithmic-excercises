from typing import Any

from hamcrest import assert_that, equal_to
from pytest_bdd import given, parsers, scenarios, then, when

from problems.euler.largest_palindrome_product import get_largest_paindrome_product, get_limits

scenarios("problems/euler/Largest Palindrome Product.feature")


@given(parsers.parse("2 {digits}-digit numbers"), converters={"digits": int}, target_fixture="context")
def given_a_limit_number(digits: int) -> dict[str, Any]:
    return {"digits": digits}


@when("I run get_largest_paindrome_product")
def when_I_run__get_largest_paindrome_product(context: dict[str, Any]) -> dict[str, Any]:
    digits: int = context["digits"]
    minimum, maximum = get_limits(digits)
    factors: tuple[int, int] = get_largest_paindrome_product(minimum, maximum)
    context["factors"] = factors

    factor1, factor2 = factors
    context["factor1"] = factor1
    context["factor2"] = factor2

    product: int = factor1 * factor2
    context["product"] = product

    return context


@then(parsers.parse("I get {factor1} and {factor2} factors"), converters={"factor1": int, "factor2": int})
def then_I_get_factors(factor1: int, factor2: int, context: dict[str, Any]) -> None:
    x = context["factor1"]
    y = context["factor2"]

    assert_that(factor1, equal_to(x))
    assert_that(factor2, equal_to(y))


@then(parsers.parse("its {product} is the largest palindrome"), converters={"product": int})
def and_its_product_ist_the_largest_palindrome(product: int, context: dict[str, Any]) -> None:
    actual_product = context["product"]
    assert_that(product, equal_to(actual_product))
