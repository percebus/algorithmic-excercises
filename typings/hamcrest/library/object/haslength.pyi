"""
This type stub file was generated by pyright.
"""

from collections.abc import Sized
from typing import Union
from hamcrest.core.base_matcher import BaseMatcher
from hamcrest.core.description import Description
from hamcrest.core.matcher import Matcher

__author__ = ...
__copyright__ = ...
__license__ = ...
class HasLength(BaseMatcher[Sized]):
    def __init__(self, len_matcher: Matcher[int]) -> None:
        ...
    
    def describe_mismatch(self, item: Sized, mismatch_description: Description) -> None:
        ...
    
    def describe_to(self, description: Description) -> None:
        ...
    


def has_length(match: Union[int, Matcher[int]]) -> Matcher[Sized]:
    """Matches if ``len(item)`` satisfies a given matcher.

    :param match: The matcher to satisfy, or an expected value for
        :py:func:`~hamcrest.core.core.isequal.equal_to` matching.

    This matcher invokes the :py:func:`len` function on the evaluated object to
    get its length, passing the result to a given matcher for evaluation.

    If the ``match`` argument is not a matcher, it is implicitly wrapped in an
    :py:func:`~hamcrest.core.core.isequal.equal_to` matcher to check for
    :equality.

    Examples::

        has_length(greater_than(6))
        has_length(5)

    """
    ...

