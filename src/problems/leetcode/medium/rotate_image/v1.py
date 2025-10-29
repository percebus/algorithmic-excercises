from typing import Iterable

from problems.leetcode.medium.rotate_image.protocol import SolutionProtocol
from problems.leetcode.medium.rotate_image.typing import MatrixType, RowType


class Solution(SolutionProtocol):
    def rotate(self, matrix: MatrixType) -> None:
        reversed_rows: Iterable[RowType] = reversed(matrix)
        new_rows: Iterable[tuple[int]] = zip(*reversed_rows)
        for i, new_row in enumerate(new_rows):
            for j, number in enumerate(new_row):
                # FIXME: I don't think this is going to work
                # Since it will overwrite values
                matrix[i][j] = number


solution = Solution()
