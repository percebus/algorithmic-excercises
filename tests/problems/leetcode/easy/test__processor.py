
from collections.abc import Generator
from unittest.mock import patch

from hamcrest import assert_that, equal_to, is_
from problems.leetcode.easy.design_parking_system.processing.processor import BatchProcessor

import pytest

from problems.leetcode.easy.design_parking_system import ParkingSystem


@pytest.fixture
def processor() -> Generator[BatchProcessor, None, None]:
    # Before each test
    processor = BatchProcessor()

    # During each test
    yield processor

    # After each test
    processor = None


def test__process__1_1_0__no_methods__returns_None(processor: BatchProcessor) -> None:
    actual_results = processor.process(["ParkingSystem"], [[1, 1, 0]])
    assert_that(actual_results, is_(equal_to([None])))


def test__process__1_1_0__no_methods__initializes_ParkingSystem_with_1_1_0(processor: BatchProcessor) -> None:
    with patch.object(ParkingSystem, "__init__", autospec=True, return_value=None) as ParkingSystem__init__:
        actual_results = processor.process(["ParkingSystem"], [[1, 1, 0]])
        assert_that(actual_results, is_(equal_to([None])))

        assert_that(ParkingSystem__init__.call_count, is_(1))

        args1, _ = ParkingSystem__init__.call_args
        args1_without_cls = args1[1:]  # remove 'cls' from args
        assert_that(args1_without_cls, is_(equal_to((1, 1, 0))))
