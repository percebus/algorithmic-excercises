from typing import Optional

from hamcrest import assert_that, equal_to

from src.problems.euler.multiples_of_3_or_5.v2 import sum_multiples

multiples = [3, 5]


def test(limit: int, expected: Optional[int] = None) -> None:
    result: int = sum_multiples(limit, multiples)
    assert_that(result, equal_to(expected))
    print("✅", end="")


def run() -> None:
    test(10, 23)
    test(1000, 233168)


if __name__ == "__main__":
    run()
