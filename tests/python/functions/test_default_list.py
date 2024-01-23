from hamcrest import assert_that, equal_to


# Array only gets defined the first time
def fn_bad_default(arr: list[int] = []) -> list[int]:
    arr.append(1)
    return arr


def fn_good_default(arr: list[int] = None) -> list[int]:
    if arr is None:
        arr = []  # always initialize a new array

    arr.append(1)
    return arr


def test__fn__empty__returns__1():
    for fn in [fn_bad_default, fn_good_default]:
        result = fn()
        assert_that(result, equal_to([1]))


def test__fn__1_2_3__returns__1_2_3_1():
    for fn in [fn_bad_default, fn_good_default]:
        result = fn([1, 2, 3])
        assert_that(result, equal_to([1, 2, 3, 1]))


def test__fn_bad_default__empty_multiple_times__has_side_effects():
    for num in range(3):
        result = fn_bad_default()

    assert_that(result, not (equal_to([1])))
    assert set(result) <= set([1, 1, 1])


def test__fn_good_default__empty_multiple_times__is_indiscreet():
    for num in range(3):
        result = fn_good_default()
        assert_that(result, equal_to([1]))
