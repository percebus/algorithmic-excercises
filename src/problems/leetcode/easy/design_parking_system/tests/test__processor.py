from collections.abc import Generator
from unittest.mock import patch

import pytest
from hamcrest import assert_that, equal_to, is_

from problems.leetcode.easy.design_parking_system import ParkingSystem
from problems.leetcode.easy.design_parking_system.car_type import CarType
from problems.leetcode.easy.design_parking_system.processing.processor import BatchProcessor


@pytest.fixture(name="batch_processor")
def fixture_batch_processor() -> Generator[BatchProcessor, None, None]:
    # Before each test
    processor = BatchProcessor()

    # During each test
    yield processor

    # After each test
    # processor = None


def test__process__1_1_0__no_methods__returns_None(batch_processor: BatchProcessor) -> None:
    actual_results = batch_processor.process(["ParkingSystem"], [[1, 1, 0]])
    assert_that(actual_results, is_(equal_to([None])))


def test__process__1_1_0__no_methods__initializes_ParkingSystem_with_1_1_0(batch_processor: BatchProcessor) -> None:
    with patch.object(ParkingSystem, "__init__", autospec=True, return_value=None) as ParkingSystem__init__:
        actual_results = batch_processor.process(["ParkingSystem"], [[1, 1, 0]])
        assert_that(actual_results, is_(equal_to([None])))

        assert_that(ParkingSystem__init__.call_count, is_(1))

        args1, _ = ParkingSystem__init__.call_args
        args1_without_cls = args1[1:]  # remove 'cls' from args
        assert_that(args1_without_cls, is_(equal_to((1, 1, 0))))


def test__process__Example_1__returns__None_True_True_False_False(batch_processor: BatchProcessor) -> None:
    invoker_names = [
        "ParkingSystem",
        "addCar",
        "addCar",
        "addCar",
        "addCar",
    ]

    arguments = [
        [1, 1, 0],
        [CarType.BIG.value],  # 1 -1 = 0 big cars
        [CarType.MEDIUM.value],  # 1 -1 = 0 medium cars
        [CarType.SMALL.value],  # False, No small spots
        [CarType.BIG.value],  # False, No big spots
    ]

    actual_results = batch_processor.process(invoker_names, arguments)
    assert_that(actual_results, is_(equal_to([None, True, True, False, False])))
