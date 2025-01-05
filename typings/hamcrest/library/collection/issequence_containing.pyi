"""
This type stub file was generated by pyright.
"""

from typing import Sequence, TypeVar, Union
from hamcrest.core.base_matcher import BaseMatcher
from hamcrest.core.description import Description
from hamcrest.core.matcher import Matcher

__author__ = ...
__copyright__ = ...
__license__ = ...
T = TypeVar("T")
class IsSequenceContaining(BaseMatcher[Sequence[T]]):
    def __init__(self, element_matcher: Matcher[T]) -> None:
        ...
    
    def describe_to(self, description: Description) -> None:
        ...
    


class IsSequenceContainingEvery(BaseMatcher[Sequence[T]]):
    def __init__(self, *element_matchers: Matcher[T]) -> None:
        ...
    
    def describe_mismatch(self, item: Sequence[T], mismatch_description: Description) -> None:
        ...
    
    def describe_to(self, description: Description) -> None:
        ...
    


def has_item(match: Union[Matcher[T], T]) -> Matcher[Sequence[T]]:
    """Matches if any element of sequence satisfies a given matcher.

    :param match: The matcher to satisfy, or an expected value for
        :py:func:`~hamcrest.core.core.isequal.equal_to` matching.

    This matcher iterates the evaluated sequence, searching for any element
    that satisfies a given matcher. If a matching element is found,
    ``has_item`` is satisfied.

    If the ``match`` argument is not a matcher, it is implicitly wrapped in an
    :py:func:`~hamcrest.core.core.isequal.equal_to` matcher to check for
    equality.

    """
    ...

def has_items(*items: Union[Matcher[T], T]) -> Matcher[Sequence[T]]:
    """Matches if all of the given matchers are satisfied by any elements of
    the sequence.

    :param match1,...: A comma-separated list of matchers.

    This matcher iterates the given matchers, searching for any elements in the
    evaluated sequence that satisfy them. If each matcher is satisfied, then
    ``has_items`` is satisfied.

    Any argument that is not a matcher is implicitly wrapped in an
    :py:func:`~hamcrest.core.core.isequal.equal_to` matcher to check for
    equality.

    """
    ...
