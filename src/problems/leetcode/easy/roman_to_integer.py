from hamcrest import assert_that, equal_to

invalid_patterns: list[str] = ["IIII", "XXXX", "CCCC", "DD"]

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


# SRC: https://leetcode.com/problems/roman-to-integer/
def roman_to_int(string: str) -> int:
    # TODO Generalize for any letter repeated more than 3 times.
    # TODO Global RegEx?
    errors = [invalid_pattern for invalid_pattern in invalid_patterns if invalid_pattern in string]

    if errors:
        raise ValueError(f"Invalid input: {string} contains invalid patterns: {', '.join(errors)}")

    values = [Symbols[char] for char in list(string)]

    length = len(values)
    for idx, value in enumerate(values):
        if idx + 1 >= length:
            continue

        if values[idx] < values[idx + 1]:
            values[idx] = value * -1

    return sum(values)


def test(string: str, expected: int) -> None:
    result = roman_to_int(string)
    assert_that(result, equal_to(expected))
    print("✅", end="")


def run() -> None:
    # Example1:
    #  * Input: s = "III"
    #  * Output: 3
    #  * Explanation: III = 3.
    test("III", expected=3)

    # Example 2:
    #  * Input: s = "LVIII"
    #  * Output: 58
    #  * Explanation: L = 50, V = 5, III = 3.
    test("LVIII", expected=58)

    # Example 3:
    #  * Input: s = "MCMXCIV"
    #  * Output: 1994
    #  * Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
    test("MCMXCIV", expected=1994)


if __name__ == "__main__":
    run()
