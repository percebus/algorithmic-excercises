from typing import Optional

from hamcrest import assert_that, equal_to

from src.problems.euler.even_fibonacci_numbers import sum_fibonacci_evens


def test(limit: int, expected: Optional[int] = None) -> None:
    result = sum_fibonacci_evens(limit)
    assert_that(result, equal_to(expected))
    print("✅", end="")


def run() -> None:
    #       2
    #       8
    test(10, expected=10)

    #       2
    #       8
    #      34
    test(100, expected=44)

    #       2
    #       8
    #      34
    #     144
    #     610
    test(1000, expected=798)

    #       2
    #       8
    #      34
    #     144
    #     610
    #    2584
    test(10000, expected=3382)

    #       2
    #       8
    #      34
    #     144
    #     610
    #    2584
    #   10946
    #   46368
    test(100000, expected=60696)

    #       2
    #       8
    #      34
    #     144
    #     610
    #    2584
    #   10946
    #   46368
    #  196418
    #  832040
    test(1000000, expected=1089154)

    #       2
    #       8
    #      34
    #     144
    #     610
    #    2584
    #   10946
    #   46368
    #  196418
    #  832040
    # 3524578
    test(4000000, expected=4613732)


if __name__ == "__main__":
    run()
