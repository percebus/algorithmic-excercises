from hamcrest import assert_that, instance_of, is_

from ..protocol import SolutionProtocol
from ..v1 import Solution


def test_Solution_kinda_issubclass_SolutionInterface() -> None:
    assert_that(issubclass(Solution, SolutionProtocol), is_(True))


def test_Solution__kinda_is__instance_of__SolutionProtocol() -> None:
    oSolution = Solution()
    assert_that(oSolution, is_(instance_of(SolutionProtocol)))
