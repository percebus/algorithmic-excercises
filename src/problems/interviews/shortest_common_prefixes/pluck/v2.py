from typing import Any, Iterator

import more_itertools

from ..types import NestedStrDict


def pluck(data: dict[str, Any | str]) -> Iterator[Any]:
    """_summary_

    Args:
        data (dict[str, Any  |  str]): A dictionary tree with common prefixes

    Returns:
        list[str]: Plucks the keys from a nested dictionary

    Example:
        {
            'b': 'bananas',
            'd': {
                'do': {
                    'dog': 'dog',
                    'dov': 'dove'},
                'du': 'duck'
                },
            'z': 'zebra'
        }
    """

    def recurse(dictionary: NestedStrDict) -> list[Any | str]:
        return [recurse(value) if isinstance(value, dict) else key for key, value in dictionary.items()]

    results = recurse(data)
    return more_itertools.collapse(results)
