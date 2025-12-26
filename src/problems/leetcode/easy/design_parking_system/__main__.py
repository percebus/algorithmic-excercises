from hamcrest import assert_that, is_  # pyright: ignore[reportUnknownVariableType] # FIXME

from problems.leetcode.easy.design_parking_system import ParkingSystem
from problems.leetcode.easy.design_parking_system.car_type import CarType


def test(actual: False, expected: False):  # type: ignore # FIXME
    assert_that(actual, is_(expected))  # pyright: ignore[reportUnknownArgumentType] # FIXME
    print("✅", end="")


def run_scenario_01() -> None:
    num_of_spots: dict[CarType, int] = {}
    num_of_spots[CarType.BIG] = 1
    num_of_spots[CarType.MEDIUM] = 1
    num_of_spots[CarType.SMALL] = 0

    # fmt: off
    parking_system = ParkingSystem(
        num_of_spots[CarType.BIG],
        num_of_spots[CarType.MEDIUM],
        num_of_spots[CarType.SMALL],
    )
    # fmt: on

    test(parking_system.addCar(carType=CarType.BIG.value), True)  # 1 -1
    test(parking_system.addCar(carType=CarType.MEDIUM.value), True)  # 1 -1
    test(parking_system.addCar(carType=CarType.SMALL.value), False)  # 0
    test(parking_system.addCar(carType=CarType.BIG.value), False)  # 0


def run() -> None:
    run_scenario_01()


if __name__ == "__main__":
    run()
