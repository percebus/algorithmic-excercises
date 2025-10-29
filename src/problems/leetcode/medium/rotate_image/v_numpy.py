from typing import TYPE_CHECKING, Any

import numpy

from problems.leetcode.medium.rotate_image._typing import MatrixType
from problems.leetcode.medium.rotate_image.protocol import SolutionProtocol
from problems.leetcode.medium.rotate_image.util import update_matrix

if TYPE_CHECKING:
    from numpy.typing import NDArray


class Solution(SolutionProtocol):
    def rotate(self, matrix: MatrixType) -> None:
        new_matrix: NDArray[Any] = numpy.rot90(matrix, -1)
        update_matrix(matrix, new_matrix)


solution = Solution()
