from src.problems.config.configuration import configuration
from src.problems.interviews.shortest_common_prefixes.categorize.v1 import categorize
from src.problems.interviews.shortest_common_prefixes.pluck.v2 import pluck


def get_prefixes(words: list[str]):
    data = categorize(words)
    if configuration.settings.debug:
        print(data)

    return list(pluck(data))
