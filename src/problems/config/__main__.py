from typing import TYPE_CHECKING

from problems.commons.printing import pprint
from problems.config.configuration import configuration

if TYPE_CHECKING:
    from problems.config.settings import Settings


def run() -> None:
    settings: Settings = configuration.settings
    pprint(settings.safe_model_dump())


if __name__ == "__main__":
    run()
