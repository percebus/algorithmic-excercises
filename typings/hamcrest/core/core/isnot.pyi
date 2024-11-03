"""
This type stub file was generated by pyright.
"""

from typing import Type, TypeVar, Union, overload
from hamcrest.core.base_matcher import BaseMatcher
from hamcrest.core.description import Description
from hamcrest.core.matcher import Matcher

__author__ = ...
__copyright__ = ...
__license__ = ...
T = TypeVar("T")
class IsNot(BaseMatcher[T]):
    def __init__(self, matcher: Matcher[T]) -> None:
        ...
    
    def describe_to(self, description: Description) -> None:
        ...
    
    def describe_mismatch(self, item: T, mismatch_description: Description) -> None:
        ...
    


@overload
def is_not(match: Type) -> Matcher[object]:
    ...

@overload
def is_not(match: Union[Matcher[T], T]) -> Matcher[T]:
    ...

def is_not(match): # -> IsNot[object]:
    """Inverts the given matcher to its logical negation.

    :param match: The matcher to negate.

    This matcher compares the evaluated object to the negation of the given
    matcher. If the ``match`` argument is not a matcher, it is implicitly
    wrapped in an :py:func:`~hamcrest.core.core.isequal.equal_to` matcher to
    check for equality, and thus matches for inequality.

    Examples::

        assert_that(cheese, is_not(equal_to(smelly)))
        assert_that(cheese, is_not(smelly))

    """
    ...

def not_(match: Union[Matcher[T], T]) -> Matcher[T]:
    """Alias of :py:func:`is_not` for better readability of negations.

    Examples::

        assert_that(alist, not_(has_item(item)))

    """
    ...

