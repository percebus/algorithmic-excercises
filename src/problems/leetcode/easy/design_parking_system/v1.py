
from problems.leetcode.easy.design_parking_system.car_type import CarType
from problems.leetcode.easy.design_parking_system.protocol import ParkingSystemProtocol


class ParkingSystem(ParkingSystemProtocol):

    ONE_SPOT: int = 1

    def __init__(self, big: int, medium: int, small: int):
        self.parking_spots: dict[CarType, int] = {}
        self.parking_spots[CarType.BIG] = big
        self.parking_spots[CarType.MEDIUM] = medium
        self.parking_spots[CarType.SMALL] = small

    @property
    def big(self) -> int:
        return self.parking_spots[CarType.BIG]

    @property
    def medium(self) -> int:
        return self.parking_spots[CarType.MEDIUM]

    @property
    def small(self) -> int:
        return self.parking_spots[CarType.SMALL]


    def addCar(self, carType: int) -> bool:
        car_type = CarType(carType)
        if self.parking_spots[car_type] < self.ONE_SPOT:
            return False

        self.parking_spots[car_type] -= self.ONE_SPOT
        return True
