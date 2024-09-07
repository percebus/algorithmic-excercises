def sum_fibonacci_evens(limit: int = 1000) -> int:
    x, y = [1, 2]
    num = y
    result = 0

    # TODO? build fibonacci separately, and then filter?
    while num <= limit:
        if (num % 2) == 0:
            result += num

        num = x + y
        x = y
        y = num

    return result
