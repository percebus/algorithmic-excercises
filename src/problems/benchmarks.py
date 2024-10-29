from src.problems.euler.multiples_of_3_or_5.benchmark.simple import run as run_multiples_of_3_or_5_simple
from src.problems.interviews.shortest_common_prefixes.pluck.benchmark.simple import run as run_pluck_simple

modules = [
    run_pluck_simple,
    run_multiples_of_3_or_5_simple,
]


def run() -> None:
    for module in modules:
        print(f"{module.__name__}", end=": ")
        module()
        print("")


if __name__ == "__main__":
    run()
