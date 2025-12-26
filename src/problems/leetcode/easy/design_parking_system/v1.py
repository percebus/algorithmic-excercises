from problems.leetcode.easy.design_parking_system.protocol import ParkingSystemProtocol


class ParkingSystem(ParkingSystemProtocol):
    def __init__(self, big: int, medium: int, small: int):
        self.cars: dict[int, int] = {}
        self.cars[1] = big
        self.cars[2] = medium
        self.cars[3] = small

    def addCar(self, carType: int) -> bool:
        if self.cars[carType] < 1:
            return False

        self.cars[carType] -= 1
        return True
