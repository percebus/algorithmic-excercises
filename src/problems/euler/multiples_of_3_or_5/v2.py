def sum_multiples(limit: int, multiples: list[int]) -> int:
    # fmt: off
    nums = set(
        num
        for multiple in multiples
        for num in range(limit)
        if (num % multiple) == 0)  # is even
    # fmt: on

    return sum(nums)
