import string
from typing import Any, Iterator, Optional

import more_itertools
from hamcrest import assert_that, equal_to

from src.problems.config import DEBUG


# FIXME change signature
# - Since is recursive, sometimes it returns strings
# - But at the end it returns a dict
def categorize(words: list[str], prefix: str = "") -> Any:
    if len(words) == 1:
        return words[0]

    result = {}
    for letter in string.ascii_lowercase:
        _prefix = prefix + letter
        subset = [word for word in words if word.startswith(_prefix)]

        if subset:
            result[_prefix] = categorize(subset, _prefix)

    return result  # type: ignore


def pluck(data: dict[str, Any | str]) -> list[str]:
    results: list[str] = []

    def recurse(dictionary: dict[str, Any | str]) -> None:
        for key, value in dictionary.items():
            if isinstance(value, str):  # it is a str
                # FIXME very inefficient
                results.append(key)
            elif isinstance(value, dict):  # it is a dict
                recurse(value)  # type: ignore
            else:
                raise ValueError(f"Unexpected type: {type(value)}")

    recurse(data)  # FIXME refactor from procdural
    return results


def pluck2(data: dict[str, Any | str]) -> Iterator[Any]:
    def recurse(dictionary: dict[str, Any | str]) -> list[Any | str]:
        return [
            recurse(value) if isinstance(value, dict) else key  # type: ignore
            for key, value in dictionary.items()
        ]

    results = recurse(data)
    return more_itertools.collapse(results)


def get_prefixes(words: list[str]):
    data = categorize(words)
    if DEBUG:
        print(data)

    # {
    #   'b': 'bananas',
    #   'd': {
    #       'do': {
    #           'dog': 'dog',
    #           'dov': 'dove'},
    #       'du': 'duck'
    #       },
    #   'z': 'zebra'
    # }

    # TODO benchmark pluck VS pluck2 performance
    return list(pluck2(data))


def test(words: list[str], expected: Optional[list[str]] = None):
    actual = get_prefixes(words)
    assert_that(expected, equal_to(actual))
    print("✅", end="")


def run():
    test([], expected=[])
    test(["dog", "zebra", "bananas"], expected=["b", "d", "z"])
    test(["dog", "zebra", "duck", "bananas"], expected=["b", "do", "du", "z"])
    test(["dog", "zebra", "duck", "dove", "bananas"], expected=["b", "dog", "dov", "du", "z"])


if __name__ == "__main__":
    run()
