from typing import Generator, Optional


def get_factors(x: int) -> Generator[tuple[int, int]]:
    nums = range(x + 1)
    return ((a, b) for a in nums for b in (num for num in nums if num >= a) if (a * b) == x)


def is_prime_number(x: int) -> bool:
    if x == 0:
        return False
    elif x == 2:
        return True
    elif x % 2 == 0:
        return False

    count: int = 0
    for pair in get_factors(x):  # type: ignore
        count += 1  # noqa: SIM113 # FIXME?
        if count > 1:
            return False

    return True


def get_prime_factors(num: int) -> Optional[int]:
    nums = [num for pair in get_factors(num) for num in pair]

    nums.sort(reverse=True)
    for num in nums:
        if is_prime_number(num):
            return num

    return None
