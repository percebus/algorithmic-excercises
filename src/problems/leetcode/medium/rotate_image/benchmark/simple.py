import timeit

from problems.commons.utils import noop
from problems.leetcode.medium.rotate_image.v1 import solution as solution_v1
from problems.leetcode.medium.rotate_image.v_google import solution as solution_google
from problems.leetcode.medium.rotate_image.v_numpy import solution as solution_numpy


def run() -> None:
    samples = 100000

    noop(solution_v1)
    versions = {
        "numpy": solution_numpy,
        "v1": solution_v1,
        "google": solution_google,
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
        result = timeit.timeit(lambda: oSolution.rotate(matrix), number=samples)  # pylint: disable=cell-var-from-loop # FIXME?
        print(f" - result: {result}")


if __name__ == "__main__":
    run()
