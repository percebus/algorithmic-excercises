from typing import Any, Protocol


class BatchProcessorProtocol(Protocol):
    def process(self, invoker_names: list[str], arguments: list[Any]) -> list[Any]:
        """Process.

        # Examples

        ## Example 1:

        ### Input
        ["ParkingSystem", "addCar", "addCar", "addCar", "addCar"]

        [[1, 1, 0]      , [1]     , [2]     , [3]     , [1]     ]

        ### Output
        [None, True, True, False, False]
        """
        ...  # pylint: disable=W2301 unnecessary-ellipsis
