from typing import List

from hamcrest import assert_that, equal_to, has_length

SHIP = 1
SPACE = 0

"""
You're playing Battleship on a grid of cells with R rows and C columns.
There are 0 or more battleships on the grid, each occupying a single distinct cell.
The cell in the ith row from the top and jth column from the left
either contains a battleship (Gi,j = 1) or doesn't (Gi,j = 0).

You're going to fire a single shot at a random cell in the grid.
You'll choose this cell uniformly at random from the R*C possible cells.
You're interested in the probability that the cell hit by your shot contains a battleship.
Your task is to implement the function getHitProbability(R, C, G) which returns this probability.
Your return value must have an absolute or relative error
of at most 10^ -6 to be considered correct.
"""


def calculate_hit_probability(rows: List[List[int]]) -> float:
    flattened = [column for row in rows for column in row]
    spaces = len(flattened)
    ships = flattened.count(SHIP)
    return ships / spaces


# pylint: disable=invalid-name
# pylint: disable=unused-argument
def getHitProbability(R: int, C: int, G: List[List[int]]) -> float:
    """
    A function that gets the probability that the cell hit by a shot contains a battleship.

    Arguments:
        R (int): Rows
        C (int): Columns
        G (List[List[int]]): Grid

    Returns:
        float: probability with an absolute or relative error of at most 10^ -6.
    """
    first_row = G[0]
    assert_that(G, has_length(R))
    assert_that(first_row, has_length(C))
    return calculate_hit_probability(G)


# pylint: enable=unused-argument


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
