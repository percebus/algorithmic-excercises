import string
from typing import Any

from ..types import NestedStrDict


def categorize(words: list[str]) -> NestedStrDict:
    def recurse(words: list[str], prefix: str = "") -> Any:  # FIXME
        if len(words) == 1:
            return words[0]

        result: NestedStrDict = {}
        for letter in string.ascii_lowercase:
            _prefix = prefix + letter
            subset = [word for word in words if word.startswith(_prefix)]

            if subset:
                result[_prefix] = recurse(subset, _prefix)

        return result

    result: NestedStrDict = recurse(words)
    return result
