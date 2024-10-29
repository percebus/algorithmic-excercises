from typing import Any, Iterator

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
    ...