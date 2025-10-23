from typing import Protocol


class SolutionProtocol(Protocol):
    def buildArray(self, nums: list[int]) -> list[int]: ...
