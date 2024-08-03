from typing import Any


def pluck(data: dict[str, Any | str]) -> list[str]:
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
