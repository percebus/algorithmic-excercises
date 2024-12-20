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
class IsSequenceOnlyContaining(BaseMatcher[Sequence[T]]):
    def __init__(self, matcher: Matcher[T]) -> None:
        ...
    
    def describe_to(self, description: Description) -> None:
        ...
    


def only_contains(*items: Union[Matcher[T], T]) -> Matcher[Sequence[T]]:
    """Matches if each element of sequence satisfies any of the given matchers.

    :param match1,...: A comma-separated list of matchers.

    This matcher iterates the evaluated sequence, confirming whether each
    element satisfies any of the given matchers.

    Example::

        only_contains(less_than(4))

    will match ``[3,1,2]``.

    Any argument that is not a matcher is implicitly wrapped in an
    :py:func:`~hamcrest.core.core.isequal.equal_to` matcher to check for
    equality.

    """
    ...

