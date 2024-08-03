import string
from typing import Any


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
