import timeit

from src.problems.interviews.shortest_common_prefixes.pluck.v1 import pluck as pluck_v1
from src.problems.interviews.shortest_common_prefixes.pluck.v2 import pluck as pluck_v2
from src.problems.interviews.shortest_common_prefixes.pluck.v2 import pluck as pluck_v3


def run():
    # fmt: off
    data = {
        'b': 'bananas',
        'd': {
            'do': {
                'dog': 'dog',
                'dov': 'dove'},
            'du': 'duck'
            },
        'z': 'zebra'
    }
    # fmt: on

    samples = 1000000

    print("pluck.v1...")
    result1 = timeit.timeit(lambda: pluck_v1(data), number=samples)
    print(f" - result: {result1}")

    print("pluck.v2...")
    result2 = timeit.timeit(lambda: pluck_v2(data), number=samples)
    print(f" - result: {result2}")

    print("pluck.v3...")
    result2 = timeit.timeit(lambda: pluck_v3(data), number=samples)
    print(f" - result: {result2}")


if __name__ == "__main__":
    run()
