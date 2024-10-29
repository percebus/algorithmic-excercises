from typing import Any


def pluck(data: dict[str, Any | str]) -> list[str]:
    results: list[str] = []

    def recurse(dictionary: dict[str, Any | str]) -> None:
        for key, value in dictionary.items():
            if isinstance(value, str):  # it is a str
                # FIXME procedural: very inefficient
                results.append(key)
            elif isinstance(value, dict):  # it is a dict
                recurse(value)  # type: ignore
            else:
                raise ValueError(f"Unexpected type: {type(value)}")

    recurse(data)
    return results
