import math


def is_prime(n: int) -> bool:
    for x in range(2, math.floor(math.sqrt(n)) + 1):  # noqa: SIM110
        if n % x == 0:
            return False

    return True
