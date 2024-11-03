from typing import TYPE_CHECKING

from src.problems.commons.printing import pprint
from src.problems.config.configuration import configuration

if TYPE_CHECKING:
    from src.problems.config.settings import Settings


def run() -> None:
    settings: Settings = configuration.settings
    pprint(settings.safe_model_dump())


if __name__ == "__main__":
    run()
