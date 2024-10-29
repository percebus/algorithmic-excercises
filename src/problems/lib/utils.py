from typing import Any


def identity(x: Any) -> Any:
    return x

# pylint: disable=unused-argument
def noop(x: Any) -> None:
    pass
# pylint: enable=unused-argument
