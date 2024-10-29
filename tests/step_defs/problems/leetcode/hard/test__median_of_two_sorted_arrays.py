from hamcrest import assert_that, equal_to, instance_of, is_
from pytest_bdd import given, parsers, scenarios, then, when

from src.problems.leetcode.hard.median_of_two_sorted_arrays import find_median
from tests.utils import assert_is_in_range

scenarios("problems/leetcode/hard/Median of Two Sorted Arrays.feature")

constraints = {
    "m": {"min": 0, "max": 1000},  # 0 <=   m   <= 1000
    "m+n": {"min": 1, "max": 2000},  # 1 <= m + n <= 2000
}


def validate_list(array, expected):
    length = len(array)
    assert_that(length, equal_to(expected))
    validate["m"](length)


def validate_lists(array1, array2):
    m = len(array1)
    n = len(array2)
    compound = m + n
    validate["m+n"](compound)


validate = {
    "m": lambda m: assert_is_in_range(m, constraints["m"]),
    "m+n": lambda x: assert_is_in_range(x, constraints["m+n"]),
    "list": validate_list,
    "lists": validate_lists,
}


@given(parsers.parse("two sorted arrays {nums1} and {nums2}"), converters={"nums1": eval, "nums2": eval}, target_fixture="context")
def given_two_sorted_arrays(nums1, nums2):
    validate["lists"](nums1, nums2)
    return {"nums1": nums1, "nums2": nums2}


@given(parsers.parse("two empty arrays {nums1} and {nums2}"), converters={"nums1": eval, "nums2": eval}, target_fixture="context")
def given_two_empty_arrays(nums1, nums2):
    context = {"nums1": nums1, "nums2": nums2}
    try:
        validate["lists"](nums1, nums2)
    except Exception as oException:
        context["exception"] = oException

    return context


@given(parsers.parse("of size {m} and {n} respectively"), converters={"m": int, "n": int})
def given_of_size_m_an_n(m, n, context):
    nums1 = context["nums1"]
    nums2 = context["nums2"]
    validate["list"](nums1, m)
    validate["list"](nums2, n)


@when("I call find_median")
def when_I_call__find_median(context):
    nums1 = context["nums1"]
    nums2 = context["nums2"]
    result = find_median(nums1, nums2)
    context["result"] = result
    return context


@then(parsers.parse("return the {median} of the two sorted arrays {merged}"), converters={"median": float, "merged": eval})
def then_it_returns_the_median(median, merged, context):
    result = context["result"]
    assert_that(median, equal_to(result))


@then("handle the exception for two empty arrays")
def then_it_handles_the_exception(context):
    oException = context["exception"]
    assert_that(oException, is_(instance_of(Exception)))
