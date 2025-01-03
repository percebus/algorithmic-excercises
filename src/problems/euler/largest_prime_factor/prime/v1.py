from typing import Generator

from src.problems.commons.utils import noop


def get_factors(x: int) -> Generator[tuple[int, int], None, None]:
    nums = range(x + 1)
    # fmt: off
    return (
        (a, b)
        for a in nums
        for b in (
            num
            for num in nums
            if num >= a)
        if (a * b) == x)
    # fmt: on


def is_prime_number(x: int) -> bool:
    if x == 0:
        return False

    if x == 2:
        return True

    if x % 2 == 0:
        return False

    # FIXME REFACTOR
    count = 0
    for pair in get_factors(x):  # type: ignore
        noop(pair)
        count += 1  # noqa: SIM113
        if count > 1:
            return False

    return True
