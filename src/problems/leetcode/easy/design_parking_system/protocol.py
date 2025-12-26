from typing import Protocol


class ParkingSystemProtocol(Protocol):

    def __init__(self, big: int, medium: int, small: int):
        ...

    def addCar(self, carType: int) -> bool:
        ...
