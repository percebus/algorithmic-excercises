from hamcrest import assert_that, equal_to

from src.problems.meta.coding.puzzles.warmup.sum_abc.v1 import getSum

# pylint: disable=invalid-name


def test(A: int, B: int, C: int, expected: int) -> None:
    result = getSum(A, B, C)
    assert_that(result, equal_to(expected))
    print("✅", end="")


def run() -> None:
    # A+B+C = 1+2+3 = 6.
    test(A=1, B=2, C=3, expected=6)

    test(A=100, B=100, C=100, expected=300)

    test(A=85, B=16, C=93, expected=194)


# pylint: enable=invalid-name


if __name__ == "__main__":
    run()
