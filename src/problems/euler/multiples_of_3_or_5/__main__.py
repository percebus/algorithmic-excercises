from typing import Optional

from hamcrest import assert_that, equal_to

from src.problems.euler.multiples_of_3_or_5.v2 import sum_multiples

multiples = [3, 5]


def test(limit: int, expected: Optional[int] = None) -> None:
    result: int = sum_multiples(limit, multiples)
    assert_that(result, equal_to(expected))
    print("✅", end="")


def run() -> None:
    # If we list all the natural numbers below 10 that are multiples of 3 or 5,
    # we get 3, 5, 6 and 9. The sum of these multiples is 23.
    test(10, expected=23)

    # Find the sum of all the multiples of 3 or 5 below 1000.
    test(1000, expected=233168)


if __name__ == "__main__":
    run()
