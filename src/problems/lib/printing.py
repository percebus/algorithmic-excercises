import pprint as _pprint
from collections.abc import Callable

oPrettyPrinter = _pprint.PrettyPrinter(indent=3)

# pprint = print
pprint: Callable[[object], None] = oPrettyPrinter.pprint
