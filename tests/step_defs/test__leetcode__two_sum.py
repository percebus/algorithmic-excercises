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

# XXX
# def parse_numbers(lines):
#     first_line = lines.split("\n")[0]
#     return [int(number) for number in first_line.split(", ")]


@given(
    parsers.parse("an array of integer {numbers}"),
    converters={"numbers": eval},
    target_fixture="context",
)
def given_array(numbers):
    length = len(numbers)
    validate["length"](length)
    map(validate["value"], numbers)
    return {"numbers": numbers}

@given(
    parsers.parse("an integer {target:d} number")
)
def given_target(context, target):
    validate["target"](target)
    context["target"] = target


@when("two_sum is invoked")
def when__two_sum(context):
    nums = context["numbers"]
    target = context["target"]
    context["result"] = two_sum(nums, target)

@then(
    parsers.parse("it returns {indexes} of the {two_numbers}"),
    converters=dict(
        indexes=eval,
        two_numbers=eval,
    ),
)
def then_returns_tuple_of_indexes(context, indexes, two_numbers):
    idx1, idx2 = indexes
    expected_num1, expected_num2 = two_numbers
    nums = context["numbers"]
    num1 = nums[idx1]
    num2 = nums[idx2]
    context["number1"] = num1
    context["number2"] = num2
    assert expected_num1 == num1, f"expected:{expected_num1}, got:{num1}"
    assert expected_num2 == num2, f"expected:{expected_num2}, got:{num2}"


@then(parsers.parse("they add up to {target:d}"))
def then_indexes_sum_target(context, target):
    num1 = context["number1"]
    num2 = context["number2"]
    result = num1 + num2
    assert result == target, f"expected:{target}, got:{result}"
