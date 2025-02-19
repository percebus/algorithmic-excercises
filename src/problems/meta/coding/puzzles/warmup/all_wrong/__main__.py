from hamcrest import assert_that, equal_to

from . import get_wrong_answers


def test(N: int, C: str, expected: str) -> None:
    result = get_wrong_answers(N, C)
    assert_that(result, equal_to(expected))
    print("✅", end="")


def run() -> None:
    # The correct answers to the 3 questions are A, B, and A, in that order.
    # Therefore, in order to get them all wrong, the 3 answers you should give are B, A, and B, in that order.
    test(N=3, C="ABA", expected="BAB")

    # The correct answers are all B, so you should answer each question with A.
    test(N=5, C="BBBBB", expected="AAAAA")


if __name__ == "__main__":
    run()
