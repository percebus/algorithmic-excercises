from ..utils import assert_is_in_range
from pytest_bdd import scenarios, given, when, then, parsers
from problems.leetcode.easy.two_sum import two_sum

scenarios("leetcode/Two Sum.feature")

constraints = {
    "value": {"min": -109, "max": 109},  # -109 <= nums[i] <= 109
    "length": {"min": 2, "max": 104},  # 2 <= nums.length <= 104
    "target": {"min": -109, "max": 109},  # -109 <= target <= 109
}

validate = {
    "value": lambda x: assert_is_in_range(x, constraints["value"]),
    "length": lambda length: assert_is_in_range(length, constraints["length"]),
    "target": lambda target: assert_is_in_range(target, constraints["target"]),
}


# @given(
#     parsers.parse("an {array} of integer numbers"),
#     converters={"array": eval},
#     target_fixture="test_case",
# )
# def given_array(array):
#     length = len(array)
#     validate["length"](length)
#     map(validate["value"], array)
#     return {"nums": array}


@given(
    parsers.parse("an [2, 7, 11, 15] of integer numbers"),
    target_fixture="test_case",
)
def given_array():
    array = [2, 7, 11, 15]
    length = len(array)
    validate["length"](length)
    map(validate["value"], array)
    return {"nums": array}



@given(parsers.parse("an integer {target:d} number"), target_fixture="test_case")
def given_target(test_case, target):
    validate["target"](target)
    test_case["target"] = target
    return test_case


@when("I call two_sum", target_fixture="test_case")
def when__two_sum(test_case):
    nums = test_case["nums"]
    target = test_case["target"]
    test_case["result"] = two_sum(nums, target)
    return test_case


@then(
    parsers.parse("return {indices} of the {two_numbers}"),
    target_fixture="test_case",
    converters=dict(
        indices=eval,
        two_numbers=eval,
    ),
)
def then_returns_indeces(test_case, indices, two_numbers):
    idx1, idx2 = indices
    expected_num1, expected_num2 = two_numbers
    nums = test_case["nums"]
    num1 = nums[idx1]
    num2 = nums[idx2]
    test_case["num1"] = num1
    test_case["num2"] = num2
    assert expected_num1 == num1, f"expected:{expected_num1}, got:{num1}"
    assert expected_num2 == num2, f"expected:{expected_num2}, got:{num2}"
    return test_case


@then(parsers.parse("they add up to {target:d}"), target_fixture="test_case")
def then_indeces_sum_target(test_case, target):
    num1 = test_case["num1"]
    num2 = test_case["num2"]
    result = num1 + num2
    assert result == target, f"expected:{target}, got:{result}"
