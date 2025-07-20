# from problems.config.configuration import configuration # TODO
from typing import TYPE_CHECKING

from .categorize import categorize
from .pluck import pluck

if TYPE_CHECKING:
    from .types import NestedStrDict


def get_prefixes(words: list[str]) -> list[str]:
    data: NestedStrDict = categorize(words)

    entries = pluck(data)
    return list(entries)
