from ..types import NestedStrDict


def pluck(data: NestedStrDict) -> list[str]:
    """_summary_

    Args:
        data (dict[str, Any  |  str]): A dictionary tree with common prefixes

    Returns
    -------
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

    def recurse(dictionary: NestedStrDict) -> None:
        for key, value in dictionary.items():
            if isinstance(value, str):  # it is a str
                # FIXME procedural: very inefficient
                results.append(key)
            # elif value is NestedStrDict:  # TODO?
            elif isinstance(value, dict):  # it is a dict  # type: ignore
                recurse(value)
            else:
                raise ValueError(f"Unexpected type: {type(value)}")

    recurse(data)
    return results
