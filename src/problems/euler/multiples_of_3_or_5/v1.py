def sum_multiples(limit: int, multiples: list[int]) -> int:
    # fmt: off
    nums = {
        num
        for num in range(limit)
        for multiple in multiples
        if (num % multiple) == 0}  # is even
    # fmt: on

    return sum(nums)
