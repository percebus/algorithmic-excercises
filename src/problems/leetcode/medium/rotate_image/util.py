from problems.leetcode.medium.rotate_image._typing import MatrixType


def update_matrix(target_matrix: MatrixType, new_matrix: MatrixType) -> None:
    for i, new_row in enumerate(new_matrix):
        for j, number in enumerate(new_row):
            target_matrix[i][j] = number
