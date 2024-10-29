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


def inverse(char: str) -> str:
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
# pylint: enable=invalid-name
