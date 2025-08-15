from typing import Optional

from problems.euler.largest_prime_factor.prime.v1 import get_factors, is_prime_number


def get_largest_prime_factor(x: int) -> Optional[int]:
    # fmt: off
    nums = [
        num
        for pair in get_factors(x)
        for num in pair]
    # fmt: on

    nums.sort(reverse=True)
    for num in nums:
        if is_prime_number(num):
            return num

    return None
