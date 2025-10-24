import timeit

from src.problems.commons.utils import noop
from src.problems.leetcode.medium.rotate_image.v0 import solution as solution_v0
from src.problems.leetcode.medium.rotate_image.v1 import solution as solution_v1
from src.problems.leetcode.medium.rotate_image.v2 import solution as solution_v2


def run() -> None:
    samples = 100000

    noop(solution_v1)
    versions = {
        "numpy": solution_v0,
        # "v1": solution_v1,  # FIXME doesn't work properly
        "v2": solution_v2,
    }

    for key, oSolution in versions.items():
        # fmt: off
        matrix = [
            [ 5,  1,  9, 11],
            [ 2,  4,  8, 10],
            [13,  3,  6,  7],
            [15, 14, 12, 16],
        ]
        # fmt: on

        print(f"{key}:")
        result = timeit.timeit(lambda: oSolution.rotate(matrix), number=samples)
        print(f" - result: {result}")


if __name__ == "__main__":
    run()
