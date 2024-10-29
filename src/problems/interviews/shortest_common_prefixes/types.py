# Recursive dictionary type
from typing import Union

NestedStrDict = dict[str, Union[str, "NestedStrDict"]]
