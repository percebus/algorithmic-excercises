from .base import SolutionBase


class Solution(SolutionBase):
    # fmt: off
    Symbols: dict[str, int] = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    # fmt: on

    invalid_patterns: list[str] = ["IIII", "XXXX", "CCCC", "DD"]

    def romanToInt(self, string: str) -> int:
        # TODO Generalize for any letter repeated more than 3 times.
        # TODO Global RegEx?
        errors = [invalid_pattern for invalid_pattern in self.invalid_patterns if invalid_pattern in string]

        if errors:
            raise ValueError(f"Invalid input: {string} contains invalid patterns: {', '.join(errors)}")

        values = [self.Symbols[char] for char in list(string)]

        length = len(values)
        for idx, value in enumerate(values):
            if idx + 1 >= length:
                continue

            if values[idx] < values[idx + 1]:
                values[idx] = value * -1

        return sum(values)


solution = Solution()
