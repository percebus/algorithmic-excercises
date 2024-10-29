def assert_is_in_range(x: int, constraint: dict[str, int]) -> None:
    minimum = constraint["min"]
    maximum = constraint["max"]
    assert minimum <= x, f"min:{minimum}, got:{x}"
    assert x <= maximum, f"max:{maximum}, got:{x}"
