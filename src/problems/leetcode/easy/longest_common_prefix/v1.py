def longest_common_prefix(words: list[str]) -> str:
    first_word: str = words[0]
    chars: list[str] = list(first_word)
    prefix: str = ""
    result: str = prefix
    for char in chars:
        prefix += char
        invalid = next((word for word in words if not word.startswith(prefix)), None)
        if invalid is None:
            result = prefix
        else:
            return result

    return result
