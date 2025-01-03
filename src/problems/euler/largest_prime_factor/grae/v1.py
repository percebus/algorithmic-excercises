from src.problems.euler.largest_prime_factor.grae.prime.v2 import is_prime

'''
Ok, let’s just iterate over every number
between 1 and 600,851,475,143,
test whether it’s prime,
then if so test whether it’s a factor of 600,851,475,143.

Finally take the biggest one and there’s your answer.
'''

def largest_prime_factor(n: int) -> list[int]:
    factors = []
    for x in range(2, n):
        if is_prime(x):  # noqa: SIM102
            if n % x == 0:
                factors.append(x)  # type: ignore

    return factors[-1]  # type: ignore
