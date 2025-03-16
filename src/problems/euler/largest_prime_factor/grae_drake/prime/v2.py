import math


def is_prime(n: int) -> bool:
    """
    Check if a number is prime.

    A prime is a number that is divisible only by 1 and itself.
    That is: it has no factors.

    Parameters
    ---------
        - `n:int`.- The number to check.

    Returns
    -------
        `bool`.- True if the number is prime, False otherwise.
    """
    for x in range(2, math.floor(math.sqrt(n)) + 1):  # noqa: SIM110
        if n % x == 0:
            return False

    return True
