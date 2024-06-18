from hamcrest import assert_that, equal_to

"""
There's a multiple-choice test with N questions, numbered from 1 to N.
Each question has 2 answer options, labelled A and B.

You know that the correct answer for the ith question is the ith character in the string C,
which is either "A" or "B", but you want to get a score of 0 on this test by answering every question incorrectly.
Your task is to implement the function getWrongAnswers(N, C) which returns a string with N characters,
the ith of which is the answer you should give for question ii in order to get it wrong (either "A" or "B").
"""

A, B = ("A", "B")
opposites = {"A": B, "B": A}


def inverse(char: str):
    return opposites[char]


def get_wrong_answers(letters: str) -> str:
    chars = list(letters)
    inversed = map(inverse, chars)
    return "".join(inversed)


# pylint: disable=invalid-name
# pylint: disable=unused-argument
def getWrongAnswers(N: int, C: str) -> str:
    return get_wrong_answers(C)


# pylint: enable=unused-argument


def test(N: int, C: str, expected: str) -> None:
    result = getWrongAnswers(N, C)
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

# pylint: enable=invalid-name
