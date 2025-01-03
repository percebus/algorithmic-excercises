from src.problems.euler.largest_prime_factor.grae.prime.v2 import is_prime


def largest_prime_factor(n: int) -> list[int]:
    factors = []
    for x in range(2, n):
        if is_prime(x):  # noqa: SIM102
            if n % x == 0:
                factors.append(x)  # type: ignore

    return factors[-1]  # type: ignore
