"""
This type stub file was generated by pyright.
"""

from typing import Optional, Sequence, TypeVar, Union
from hamcrest.core.base_matcher import BaseMatcher
from hamcrest.core.description import Description
from hamcrest.core.matcher import Matcher

__author__ = ...
__copyright__ = ...
__license__ = ...
T = TypeVar("T")
class MatchInAnyOrder:
    def __init__(self, matchers: Sequence[Matcher[T]], mismatch_description: Optional[Description]) -> None:
        ...
    
    def matches(self, item: T) -> bool:
        ...
    
    def isfinished(self, item: Sequence[T]) -> bool:
        ...
    
    def isnotsurplus(self, item: T) -> bool:
        ...
    
    def ismatched(self, item: T) -> bool:
        ...
    


class IsSequenceContainingInAnyOrder(BaseMatcher[Sequence[T]]):
    def __init__(self, matchers: Sequence[Matcher[T]]) -> None:
        ...
    
    def matches(self, item: Sequence[T], mismatch_description: Optional[Description] = ...) -> bool:
        ...
    
    def describe_mismatch(self, item: Sequence[T], mismatch_description: Description) -> None:
        ...
    
    def describe_to(self, description: Description) -> None:
        ...
    


def contains_inanyorder(*items: Union[Matcher[T], T]) -> Matcher[Sequence[T]]:
    """Matches if sequences's elements, in any order, satisfy a given list of
    matchers.

    :param match1,...: A comma-separated list of matchers.

    This matcher iterates the evaluated sequence, seeing if each element
    satisfies any of the given matchers. The matchers are tried from left to
    right, and when a satisfied matcher is found, it is no longer a candidate
    for the remaining elements. If a one-to-one correspondence is established
    between elements and matchers, ``contains_inanyorder`` is satisfied.

    Any argument that is not a matcher is implicitly wrapped in an
    :py:func:`~hamcrest.core.core.isequal.equal_to` matcher to check for
    equality.

    """
    ...
