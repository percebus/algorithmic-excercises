# from src.problems.config.configuration import configuration # TODO
from src.problems.interviews.shortest_common_prefixes.categorize import categorize
from src.problems.interviews.shortest_common_prefixes.pluck import pluck


def get_prefixes(words: list[str]):
    data = categorize(words)

    # FIXME add logger
    # if configuration.settings.debug:
    #     print(data)

    entries = pluck(data)
    return list(entries)
