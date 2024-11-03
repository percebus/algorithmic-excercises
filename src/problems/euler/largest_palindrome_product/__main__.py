import logging

from hamcrest import assert_that, equal_to

from src.problems.euler.largest_palindrome_product.v1 import format_pair, get_largest_paindrome_product, get_limits


def test(chars: int, product: int, expected: tuple[int, int]) -> None:
    minimum, maximum = get_limits(chars)
    result: tuple[int, int] = get_largest_paindrome_product(minimum, maximum)
    logging.debug("chars:%d, product:%d, expected:%s, minimum:%d, maximum:%d -> result:%d", chars, product, expected, minimum, maximum, result)
    assert_that(format_pair(result), equal_to(format_pair(expected)))
    x, y = result
    _product = x * y
    assert_that(_product, equal_to(product))
    print("✅", end="")


def run() -> None:
    test(chars=2, product=9009, expected=(91, 99))
    test(chars=3, product=906609, expected=(913, 993))


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    run()
