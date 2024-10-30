from typing import TYPE_CHECKING

from src.problems.config.configuration import configuration
from src.problems.lib.printing import pprint

if TYPE_CHECKING:
    from src.problems.config.settings import Settings


def run() -> None:
    settings: Settings = configuration.settings
    pprint(settings.safe_model_dump())


if __name__ == "__main__":
    run()
