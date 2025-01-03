"""
This type stub file was generated by pyright.
"""

from abc import ABCMeta, abstractmethod
from hamcrest.core.base_matcher import BaseMatcher
from hamcrest.core.description import Description

__author__ = ...
__copyright__ = ...
__license__ = ...
class SubstringMatcher(BaseMatcher[str], metaclass=ABCMeta):
    def __init__(self, substring) -> None:
        ...
    
    def describe_to(self, description: Description) -> None:
        ...
    
    @abstractmethod
    def relationship(self): # -> None:
        ...
    


