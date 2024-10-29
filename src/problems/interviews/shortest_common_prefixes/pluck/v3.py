from typing import Any, Iterator

import more_itertools


def pluck(data: dict[str, Any | str]) -> Iterator[Any]:
    def recurse(dictionary: dict[str, Any | str]) -> list[Any | str]:
        return (  # only changed [] for ()
            recurse(value) if isinstance(value, dict) else key  # type: ignore
            for key, value in dictionary.items()
        )

    results = recurse(data)
    return more_itertools.collapse(results)
