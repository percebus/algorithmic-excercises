import string
from typing import Any

from src.problems.config.configuration import configuration


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


def get_prefixes(words: list[str]):
    data = categorize(words)
    if configuration.settings.debug:
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
