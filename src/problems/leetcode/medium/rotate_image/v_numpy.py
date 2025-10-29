from typing import TYPE_CHECKING, Any

import numpy

from problems.leetcode.medium.rotate_image.protocol import SolutionProtocol
from problems.leetcode.medium.rotate_image.typing import MatrixType

if TYPE_CHECKING:
    from numpy.typing import NDArray


class Solution(SolutionProtocol):
    def rotate(self, matrix: MatrixType) -> None:
        new_matrix: NDArray[Any] = numpy.rot90(matrix, -1)

        # matrix = new_matrix  # This does NOT work
        for i, new_row in enumerate(new_matrix):
            for j, number in enumerate(new_row):
                matrix[i][j] = number


solution = Solution()
