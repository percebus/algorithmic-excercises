import timeit

from src.problems.euler.multiples_of_3_or_5.nayuki import sum_multiples as sum_multiples_nayuki
from src.problems.euler.multiples_of_3_or_5.v1 import sum_multiples as sum_multiples_v1
from src.problems.euler.multiples_of_3_or_5.v2 import sum_multiples as sum_multiples_v2


def run() -> None:
    limit = 1000
    samples = 100000
    multiples = [3, 5]

    print("Nayuki's...")
    result1 = timeit.timeit(lambda: sum_multiples_nayuki(limit), number=samples)
    print(f" - result: {result1}")

    print("v1...")
    result2 = timeit.timeit(lambda: sum_multiples_v1(limit, multiples), number=samples)
    print(f" - result: {result2}")

    print("v2...")
    result2 = timeit.timeit(lambda: sum_multiples_v2(limit, multiples), number=samples)
    print(f" - result: {result2}")


if __name__ == "__main__":
    run()
