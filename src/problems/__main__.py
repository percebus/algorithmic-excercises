import logging

# TODO make each module self contained and importable
# TODO or perhaps look recursively for all '__main__' modules in the problems directory
from src.problems.euler.even_fibonacci_numbers import __main__ as sum_fibonacci_evens
from src.problems.euler.largest_palindrome_product import __main__ as largest_palindrome_product
from src.problems.euler.largest_prime_factor import __main__ as largest_prime_factor
from src.problems.euler.multiples_of_3_or_5 import __main__ as multiples_of_3_or_5
from src.problems.interviews.shortest_common_prefixes import __main__ as shortest_common_prefixes
from src.problems.leetcode.easy.longest_common_prefix import __main__ as longest_common_prefix
from src.problems.leetcode.easy.palindrome_number import __main__ as palindrome_number
from src.problems.leetcode.easy.reverse_string import __main__ as reverse_string
from src.problems.leetcode.easy.roman_to_integer import __main__ as roman_to_integer
from src.problems.leetcode.easy.two_sum import __main__ as two_sum
from src.problems.leetcode.easy.valid_parentheses import __main__ as valid_parentheses
from src.problems.leetcode.hard.median_of_two_sorted_arrays import __main__ as median_of_two_sorted_arrays
from src.problems.meta.coding.puzzles.warmup.all_wrong import __main__ as all_wrong
from src.problems.meta.coding.puzzles.warmup.battleship import __main__ as battleship
from src.problems.meta.coding.puzzles.warmup.sum_abc import __main__ as sum_abc

# fmt: off
modules = [
    sum_fibonacci_evens,
    largest_palindrome_product,
    largest_prime_factor,
    multiples_of_3_or_5,
    shortest_common_prefixes,
    longest_common_prefix,
    palindrome_number,
    reverse_string,
    roman_to_integer,
    two_sum,
    valid_parentheses,
    median_of_two_sorted_arrays,
    all_wrong,
    battleship,
    sum_abc,
]
# fmt: on


def run() -> None:
    logging.basicConfig(level=logging.INFO)
    logging.info("Running all problems vvv")
    for module in modules:
        print(f"{module.__name__}", end=": ")
        module.run()
        print("")  # Force a \n
    logging.info("All problems ^^^ ran successfully!")


if __name__ == "__main__":
    run()
