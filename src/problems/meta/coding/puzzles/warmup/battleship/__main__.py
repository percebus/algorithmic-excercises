from typing import List

from hamcrest import assert_that, equal_to

from . import getHitProbability

# pylint: disable=invalid-name


def test(R: int, C: int, G: List[List[int]], expected: float) -> None:
    result = getHitProbability(R, C, G)
    assert_that(result, equal_to(expected))
    print("✅", end="")


def run() -> None:
    # 3 of the 6 cells in the grid contain battleships.
    # Therefore, the probability that your shot will hit one of them is 3/6 = 0.5
    test(R=2, C=3, G=[[0, 0, 1], [1, 0, 1]], expected=0.5)

    # all 4cells contain battleships,
    # resulting in a probability of 1.0 of hitting a battleship.
    test(R=2, C=2, G=[[1, 1], [1, 1]], expected=1.0)


if __name__ == "__main__":
    run()

# pylint: enable=invalid-name
