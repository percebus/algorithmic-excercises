import logging

# TODO make each module self contained and importable
# TODO or perhaps look recursively for all '__main__' modules in the problems directory
from problems.euler.even_fibonacci_numbers import __main__ as sum_fibonacci_evens
from problems.euler.largest_palindrome_product import __main__ as largest_palindrome_product
from problems.euler.largest_prime_factor import __main__ as largest_prime_factor
from problems.euler.multiples_of_3_or_5 import __main__ as multiples_of_3_or_5
from problems.interviews.shortest_common_prefixes import __main__ as shortest_common_prefixes
from problems.leetcode.easy.longest_common_prefix import __main__ as longest_common_prefix
from problems.leetcode.easy.merge_two_sorted_lists import __main__ as merge_two_sorted_lists
from problems.leetcode.easy.palindrome_number import __main__ as palindrome_number
from problems.leetcode.easy.reverse_string import __main__ as reverse_string
from problems.leetcode.easy.roman_to_integer import __main__ as roman_to_integer
from problems.leetcode.easy.two_sum import __main__ as two_sum
from problems.leetcode.easy.valid_parentheses import __main__ as valid_parentheses
from problems.leetcode.hard.median_of_two_sorted_arrays import __main__ as median_of_two_sorted_arrays
from problems.meta.coding.puzzles.warmup.all_wrong import __main__ as all_wrong
from problems.meta.coding.puzzles.warmup.battleship import __main__ as battleship
from problems.meta.coding.puzzles.warmup.sum_abc import __main__ as sum_abc

# fmt: off
modules = [
    all_wrong,
    battleship,
    largest_palindrome_product,
    largest_prime_factor,
    longest_common_prefix,
    median_of_two_sorted_arrays,
    merge_two_sorted_lists,
    multiples_of_3_or_5,
    palindrome_number,
    reverse_string,
    roman_to_integer,
    shortest_common_prefixes,
    sum_abc,
    sum_fibonacci_evens,
    two_sum,
    valid_parentheses,
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
