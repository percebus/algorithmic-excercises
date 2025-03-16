def is_prime(n: int) -> bool:
    """
    A prime is a number that is divisible only by 1 and itself.
    That is: it has no factors.
    """
    for x in range(2, n):  # noqa: SIM110
        if n % x == 0:
            return False
    return True
