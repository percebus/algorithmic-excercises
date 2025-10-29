from typing import Protocol


# SRC: https://leetcode.com/problems/rotate-image/description/
class SolutionProtocol(Protocol):
    def rotate(self, matrix: list[list[int]]) -> None:
        # Do not return anything, modify matrix in-place instead.
        ...
