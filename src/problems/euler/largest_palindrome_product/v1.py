import logging
from typing import Optional

from problems.commons.palindromes.check.reversing import is_palindrome


def get_limits(chars: int) -> tuple[int, int]:
    _minimum = "1" + "".join("0" for _ in range(0, chars - 1))
    minimum = int(_minimum)

    _maximum = "".join("9" for _ in range(0, chars))
    maximum = int(_maximum)
    return minimum, maximum


def get_largest_paindrome_product(minimum: int, maximum: int) -> tuple[int, int]:
    ceiling = maximum * maximum
    results: list[Optional[tuple[int, int]]] = [None] * (ceiling + 1)

    # FIXME brute force
    for x in reversed(range(minimum, maximum + 1)):
        for y in reversed(range(x, maximum + 1)):
            product = x * y
            product_str = str(product)
            if is_palindrome(product_str):
                logging.debug("%dx%d = %d", x, y, product)
                results.insert(product + 1, (x, y))

    palindromes = [result for result in results if result]
    logging.debug("palindromes: %s", palindromes)
    return palindromes[-1]
