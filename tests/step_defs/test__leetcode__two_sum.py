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

def parse_numbers(lines):
    first_line = lines.split("\n")[0]
    return [
        int(number)
        for number in
        first_line.split(", ")
    ]


@given(
    parsers.parse("an {array} of integer numbers"),
    converters={"array": eval},
    target_fixture="test_case",
)
def given_array(array):
    length = len(array)
    validate["length"](length)
    map(validate["value"], array)
    return {"nums": array}


@given(
    parsers.parse("some integer {numbers}"),
    converters={"numbers": parse_numbers},
    target_fixture="test_case",
)
def given_array(array):
    length = len(array)
    validate["length"](length)
    map(validate["value"], array)
    return {"nums": array}


@given(parsers.parse("an integer {target:d} number"), target_fixture="test_case")
def given_target(test_case, target):
    validate["target"](target)
    test_case["target"] = target
    return test_case


@when("two_sum is invoked", target_fixture="test_case")
def when__two_sum(test_case):
    nums = test_case["nums"]
    target = test_case["target"]
    test_case["result"] = two_sum(nums, target)
    return test_case


@then(
    parsers.parse("it returns a tuple of {indices} of the {two_numbers}"),
    target_fixture="test_case",
    converters=dict(
        indices=eval,
        two_numbers=parse_numbers,
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


@then(
    parsers.parse("it returns a 2 {indices} of the {two_numbers}"),
    target_fixture="test_case",
    converters=dict(
        indices=parse_numbers,
        two_numbers=parse_numbers,
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
