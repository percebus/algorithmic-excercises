from typing import Any

from hamcrest import assert_that, equal_to

from problems.leetcode.easy.design_parking_system import ParkingSystem, processor
from problems.leetcode.easy.design_parking_system.car_type import CarType


def test_results(actual: list[Any], expected: list[Any]) -> None:
    assert_that(actual, equal_to(expected))
    print("✅", end="")


def test(invoker_names: list[str], arguments: list[Any], expected_results: list[Any]) -> None:
    actual_results = processor.process(invoker_names, arguments)
    assert_that(actual_results, equal_to(expected_results))
    print("✅", end="")


def run_Example_1_directly() -> None:
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

    # fmt: off
    results = [
        parking_system.addCar(carType=CarType.BIG.value)   ,  # 1 -1 = 0 big cars
        parking_system.addCar(carType=CarType.MEDIUM.value),  # 1 -1 = 0 medium cars
        parking_system.addCar(carType=CarType.SMALL.value) ,  # 0
        parking_system.addCar(carType=CarType.BIG.value)   ,  # 0
    ]
    # fmt: on

    test_results(results, [True, True, False, False])


def run_Example_1_via_processor() -> None:
    num_of_spots: dict[CarType, int] = {}
    num_of_spots[CarType.BIG] = 1
    num_of_spots[CarType.MEDIUM] = 1
    num_of_spots[CarType.SMALL] = 0

    init_args = [
        num_of_spots[CarType.BIG],
        num_of_spots[CarType.MEDIUM],
        num_of_spots[CarType.SMALL],
    ]

    big = CarType.BIG.value
    medium = CarType.MEDIUM.value
    small = CarType.SMALL.value

    # fmt: off
    # Inputs
    invoker_names    = ["ParkingSystem", "addCar", "addCar", "addCar", "addCar"]
    arguments        = [init_args      , [big]   , [medium], [small] , [big]   ]
    # Outputs
    expected_results = [None           , True    , True    , False   , False   ]
    # fmt: on

    test(invoker_names, arguments, expected_results)


def run() -> None:
    run_Example_1_directly()
    run_Example_1_via_processor()


if __name__ == "__main__":
    run()
