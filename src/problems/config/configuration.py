import json
import logging
from dataclasses import dataclass, field

# NOTE: This import is needed to properly configure logging
from logging import config  # type: ignore # pylint: disable=W0611 # noqa
from typing import Any, Optional

from src.problems.config.settings import Settings


@dataclass
class Configuration:
    settings: Settings = field(default_factory=Settings)

    # pylint: disable=W0108 # unnecessary-lambda
    logging: Optional[dict[str, Any]] = field(init=False, default=None)
    # pylint: enable=W0108

    def configure_logging(self) -> None:
        _path: str = self.settings.logging_config or ""

        with open(_path, "r", encoding="utf-8") as f:
            logging_config = json.load(f)

        logging.config.dictConfig(logging_config)  # type: ignore
        logging.getLogger(__name__).debug("Configuration: initializing...")

    def __post_init__(self) -> None:
        self.configure_logging()


configuration = Configuration()
