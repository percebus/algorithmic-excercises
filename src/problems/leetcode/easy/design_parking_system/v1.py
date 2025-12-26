from problems.leetcode.easy.design_parking_system.protocol import ParkingSystemProtocol


class ParkingSystem(ParkingSystemProtocol):
    def __init__(self, big: int, medium: int, small: int):
        self.parking_spots: dict[int, int] = {}
        self.parking_spots[1] = big
        self.parking_spots[2] = medium
        self.parking_spots[3] = small

    def addCar(self, carType: int) -> bool:
        if self.parking_spots[carType] < 1:
            return False

        self.parking_spots[carType] -= 1
        return True
