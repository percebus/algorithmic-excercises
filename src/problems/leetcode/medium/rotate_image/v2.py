from src.problems.leetcode.medium.rotate_image.protocol import SolutionProtocol
from src.problems.leetcode.medium.rotate_image.typing import MatrixType


# Google's Solution (Gemini?)
class Solution(SolutionProtocol):
    def rotate(self, matrix: MatrixType) -> None:
        rows = matrix
        num_of_columns: int = len(matrix)
        for i, _ in enumerate(rows):
            for j in range(i + 1, num_of_columns):  # Iterate through the upper triangle
                a, b = matrix[i][j], matrix[j][i]
                matrix[i][j], matrix[j][i] = b, a
            matrix[i].reverse()  # XXX FIXME


solution = Solution()
