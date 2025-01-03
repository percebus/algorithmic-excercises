from typing import Optional

from hamcrest import assert_that, equal_to

from src.problems.euler.largest_prime_factor import get_largest_prime_factor


def test(x: int, expected: Optional[int] = None) -> None:
    result = get_largest_prime_factor(x)
    assert_that(result, equal_to(expected))
    print("✅", end="")


def run() -> None:
    # The prime factors of 13195 are 5, 7, 13 and 29.
    test(13195, expected=29)

    # What is the largest prime factor of the number 600851475143 ?
    test(600851475143, expected=6857)


if __name__ == "__main__":
    run()
