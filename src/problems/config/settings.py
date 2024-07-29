from typing import Optional

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # NOTE: os.environ takes precedence over .env files
    model_config = SettingsConfigDict(
        extra="ignore",
        case_sensitive=False,
        env_file=(  # Each file overrides the previous one
            ".env",  # lowest precedence
            ".env.local",  # highest precedence
        ),
    )

    debug: Optional[bool] = Field(default=False)

    # pylint: disable=W0108 # unnecessary-lambda
    logging_config: Optional[str] = Field(default="data/config/logging.json")
    # pylint: enable=W0108

    def safe_model_dump(self):
        return self.model_dump() if self.debug else None
