"""
This type stub file was generated by pyright.
"""

from hamcrest.core.matcher import Matcher
from hamcrest.library.text.substringmatcher import SubstringMatcher

__author__ = ...
__copyright__ = ...
__license__ = ...
class StringStartsWith(SubstringMatcher):
    def __init__(self, substring) -> None:
        ...
    
    def relationship(self): # -> Literal['starting with']:
        ...
    


def starts_with(substring: str) -> Matcher[str]:
    """Matches if object is a string starting with a given string.

    :param string: The string to search for.

    This matcher first checks whether the evaluated object is a string. If so,
    it checks if ``string`` matches the beginning characters of the evaluated
    object.

    Example::

        starts_with("foo")

    will match "foobar".

    """
    ...

