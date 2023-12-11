import string
from pytest_bdd import scenarios, given, when, then, parsers
from ..utils import assert_is_in_range
from problems.leetcode.easy.longest_common_prefix import longest_common_prefix

scenarios("leetcode/easy/Longest Common Prefix.feature")

# TODO: Enhance
# consists of only lower-case English letters.
valid_chars = list(string.ascii_lowercase) + [""]

constraints = {
    "word": {"min": 0, "max": 200},  # 0 <= strs[i].length <= 200
    "words": {"min": 1, "max": 200},  # 1 <= strs.length <= 200
}


def validate_chars(word):
    for char in list(word):
        if char not in valid_chars:
            raise Exception("invalid character")
    return True


def validate_word(word):
    assert_is_in_range(len(word), constraints["word"])
    validate_chars(word)
    return True


def validate_words(words):
    assert_is_in_range(len(words), constraints["words"])
    for word in words:
        validate_word(word)
    return True


validate = {"word": validate_word, "words": validate_words}


def clean(word):
    return word.replace("''", "")


def parse(words):
    return [clean(word) for word in words.split(", ")]


@given(
    parsers.parse("some {words}"),
    converters={"words": parse},
    target_fixture="context",
)
def given_some_words(words):
    validate["words"](words)
    return {"strings": words}


@when("I call longest_common_prefix")
def when__longest_common_prefix(context):
    strings = context["strings"]
    context["result"] = longest_common_prefix(strings)


@then(
    parsers.parse(
        "find the longest common {prefix} string amongst an array of strings"
    ),
    converters={"prefix": clean},
)
def then_it_matches(context, prefix):
    result = context["result"]
    assert result == prefix, f"expected:'{prefix}', got:{result}"


@given(
    parsers.parse("an array of invalid {strings}"),
    converters={"strings": parse},
    target_fixture="context",
)
def given_invalid_strings(strings):
    try:
        validate["words"](strings)
    except Exception as exception:
        return {"strings": strings, "exception": exception}


@then("returns an empty string")
def then_is_empty(context):
    prefix = ""
    result = context["result"]
    assert result == prefix, f"expected:'{prefix}', got:'{result}'"


@then("handle the exception for the invalid chars")
def then_handle_exception(context):
    oException = context["exception"]
    assert isinstance(oException, Exception), f"expected:Exception, got:{oException}"
