from hamcrest import assert_that, equal_to

"""
Given three integers A, B, and C, determine their sum.

Your task is to implement the function getSum(A, B, C)
which returns the sum A+B+C.
"""


def calculate_sum(a: int, b: int, c: int) -> int:
    return a + b + c


# pylint: disable=invalid-name
def getSum(A: int, B: int, C: int) -> int:
    return calculate_sum(A, B, C)


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
