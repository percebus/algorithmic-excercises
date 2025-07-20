import math

from problems.euler.largest_prime_factor.grae_drake.prime.v2 import is_prime


def largest_prime_factor(n: int) -> int:
    factors = []
    for x in range(2, math.floor(math.sqrt(n)) + 1):
        if is_prime(x):  # noqa: SIM102
            if n % x == 0:
                pair = n / x  # type: ignore
                factors.append(x)  # type: ignore
                if is_prime(pair):  # type: ignore
                    factors.append(pair)  # type: ignore

    return sorted(factors)[-1]  # type: ignore
