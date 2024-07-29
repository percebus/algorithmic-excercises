from src.problems.config.configuration import configuration
from src.problems.config.settings import Settings
from src.problems.lib.printing import pprint


def run() -> None:
    settings: Settings = configuration.settings
    pprint(settings.safe_model_dump())


if __name__ == "__main__":
    run()
