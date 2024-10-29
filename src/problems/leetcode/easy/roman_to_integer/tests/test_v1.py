from hamcrest import assert_that, instance_of, is_

from ..base import SolutionBase
from ..v1 import Solution


def test_Solution_issubclass_SolutionBase() -> None:
    assert_that(issubclass(Solution, SolutionBase), is_(True))


def test_Solution__is__instance_of__SolutionInterface() -> None:
    oSolution = Solution()
    assert_that(oSolution, is_(instance_of(SolutionBase)))
