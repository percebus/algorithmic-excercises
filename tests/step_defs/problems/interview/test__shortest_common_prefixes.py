from hamcrest import assert_that, equal_to
from pytest_bdd import given, parsers, scenarios, then, when

# NOTE: v1 is actually faster
from problems.interviews.shortest_common_prefixes import get_prefixes

scenarios("problems/interviews/Shortest Common Prefixes.feature")


def clean(word):
    return word.replace("''", "")


def parse(words):
    return [clean(word) for word in words.split(", ")]


@given(parsers.parse("a list of {words}"), converters={"words": parse}, target_fixture="context")
def given_a_list_of_words(words):
    return {"words": words}


@when("I call shortest_common_prefixes")
def when_I_call__shortest_common_prefixes(context):
    words = context["words"]
    result = get_prefixes(words)
    context["result"] = result
    return context


@then(parsers.parse("find the shortest common {prefixes} strings amongst an array of strings"), converters={"prefixes": parse})
def then_it_finds_the_shortest_common_prefix(prefixes, context):
    result = context["result"]
    assert_that(prefixes, equal_to(result))
