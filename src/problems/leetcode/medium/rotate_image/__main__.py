from hamcrest import assert_that, equal_to

from problems.leetcode.medium.rotate_image import rotate
from problems.leetcode.medium.rotate_image._typing import MatrixType


def test(matrix: MatrixType, expected: MatrixType) -> None:
    rotate(matrix)  # Procedural
    assert_that(matrix, equal_to(expected))
    print("✅", end="")


def run() -> None:
    # Example 1:
    #
    # * Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
    # * Output: [[7,4,1],[8,5,2],[9,6,3]]
    # fmt: off
    input1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]
    # fmt: on

    # fmt: off
    output1 = [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3]]
    # fmt: on
    test(input1, expected=output1)

    # Example 2:
    #
    # * Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    # * Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
    # fmt: off
    input2 = [
        [ 5,  1,  9, 11],
        [ 2,  4,  8, 10],
        [13,  3,  6,  7],
        [15, 14, 12, 16]]
    # fmt: on

    # fmt: off
    output2 = [
        [15, 13,  2,  5],
        [14,  3,  4,  1],
        [12,  6,  8,  9],
        [16,  7, 10, 11]]
    # fmt: on
    test(input2, expected=output2)


if __name__ == "__main__":
    run()
