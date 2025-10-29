from typing import Iterable

from problems.leetcode.medium.rotate_image._typing import MatrixType, RowType
from problems.leetcode.medium.rotate_image.protocol import SolutionProtocol
from problems.leetcode.medium.rotate_image.util import update_matrix


class Solution(SolutionProtocol):
    def rotate(self, matrix: MatrixType) -> None:
        reversed_rows: Iterable[RowType] = reversed(matrix)
        new_rows: Iterable[tuple[int]] = zip(*reversed_rows)

        # Create a copy and update
        # FIXME do in-place without extra memory allocation
        copied_matrix = [list(row) for row in new_rows]
        update_matrix(matrix, copied_matrix)


solution = Solution()
