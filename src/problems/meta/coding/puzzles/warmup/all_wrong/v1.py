from src.problems.meta.coding.puzzles.warmup.all_wrong.base import PuzzleInterface


class Puzzle(PuzzleInterface):
    A, B = ("A", "B")
    opposites = {"A": B, "B": A}

    @classmethod
    def inverse(cls, char: str) -> str:
        return cls.opposites[char]

    @classmethod
    def _get_wrong_answers(cls, letters: str) -> str:
        chars = list(letters)
        inversed = map(cls.inverse, chars)
        return "".join(inversed)

    # pylint: disable=invalid-name
    # pylint: disable=unused-argument
    def getWrongAnswers(self, numOfQuestions: int, letters: str) -> str:
        return self._get_wrong_answers(letters)

    # pylint: enable=unused-argument
    # pylint: enable=invalid-name


puzzle = Puzzle()
