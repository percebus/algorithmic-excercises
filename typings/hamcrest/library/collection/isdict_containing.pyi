"""
This type stub file was generated by pyright.
"""

from typing import Hashable, Mapping, TypeVar, Union
from hamcrest.core.base_matcher import BaseMatcher
from hamcrest.core.description import Description
from hamcrest.core.matcher import Matcher

__author__ = ...
__copyright__ = ...
__license__ = ...
K = TypeVar("K", bound=Hashable)
V = TypeVar("V")
class IsDictContaining(BaseMatcher[Mapping[K, V]]):
    def __init__(self, key_matcher: Matcher[K], value_matcher: Matcher[V]) -> None:
        ...
    
    def describe_to(self, description: Description) -> None:
        ...
    
    def describe_mismatch(self, item: Mapping[K, V], mismatch_description: Description) -> None:
        ...
    
    def describe_match(self, item: Mapping[K, V], match_description: Description) -> None:
        ...
    


def has_entry(key_match: Union[K, Matcher[K]], value_match: Union[V, Matcher[V]]) -> Matcher[Mapping[K, V]]:
    """Matches if dictionary contains key-value entry satisfying a given pair
    of matchers.

    :param key_match: The matcher to satisfy for the key, or an expected value
        for :py:func:`~hamcrest.core.core.isequal.equal_to` matching.
    :param value_match: The matcher to satisfy for the value, or an expected
        value for :py:func:`~hamcrest.core.core.isequal.equal_to` matching.

    This matcher iterates the evaluated dictionary, searching for any key-value
    entry that satisfies ``key_match`` and ``value_match``. If a matching entry
    is found, ``has_entry`` is satisfied.

    Any argument that is not a matcher is implicitly wrapped in an
    :py:func:`~hamcrest.core.core.isequal.equal_to` matcher to check for
    equality.

    Examples::

        has_entry(equal_to('foo'), equal_to(1))
        has_entry('foo', 1)

    """
    ...

