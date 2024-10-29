from hamcrest import assert_that, equal_to

from . import roman_to_int


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
