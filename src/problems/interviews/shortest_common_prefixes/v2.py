import string
from typing import Any, Iterator

import more_itertools

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


def pluck(data: dict[str, Any | str]) -> Iterator[Any]:
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
    return list(pluck(data))
