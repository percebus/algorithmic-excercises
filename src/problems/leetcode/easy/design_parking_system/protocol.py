from typing import Protocol


# SRC: https://leetcode.com/problems/design-parking-system/description/
class ParkingSystemProtocol(Protocol):
    def __init__(self, big: int, medium: int, small: int): ...

    def addCar(self, carType: int) -> bool: ...
