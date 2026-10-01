"""Validated settings with environment, dotenv and TOML precedence."""

import os
from pathlib import Path
from typing import Annotated, Literal

from pydantic import Field, StringConstraints
from pydantic_settings import (
    BaseSettings,
    DotEnvSettingsSource,
    PydanticBaseSettingsSource,
    SettingsConfigDict,
    TomlConfigSettingsSource,
)


def _config_directory() -> Path:
    configured = os.environ.get("BRANCHSTATE_CONFIG_DIR")
    if configured is None:
        return Path(__file__).resolve().parents[2]

    directory = Path(configured)
    if not directory.is_absolute() or not directory.is_dir():
        raise ValueError(
            "BRANCHSTATE_CONFIG_DIR must be an existing absolute directory"
        )
    return directory.resolve()


class StrictDotEnvSettingsSource(DotEnvSettingsSource):
    """Keep unknown empty/bare keys so model validation can reject them."""

    def __call__(self) -> dict[str, object]:
        data = super().__call__()
        known_names = {
            f"{self.env_prefix}{name}" for name in self.settings_cls.model_fields
        }
        if not self.case_sensitive:
            known_names = {name.lower() for name in known_names}
        for name, value in self.env_vars.items():
            if not value and name not in known_names:
                data[name] = value
        return data


class Settings(BaseSettings):
    """Load configuration only from the declared sources, never constructor values."""

    model_config = SettingsConfigDict(
        env_prefix="BRANCHSTATE_",
        extra="forbid",
        env_ignore_empty=False,
        validate_default=True,
        cli_parse_args=None,
    )

    app_name: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)] = (
        Field()
    )
    environment: Literal["development", "test", "production"] = "development"

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        directory = _config_directory()
        return (
            env_settings,
            StrictDotEnvSettingsSource(
                settings_cls,
                env_file=directory / ".env",
                env_file_encoding="utf-8",
            ),
            TomlConfigSettingsSource(settings_cls, toml_file=directory / "config.toml"),
        )


def load_settings() -> Settings:
    """Read and validate the current sources without caching or import side effects."""
    # BaseSettings obtains required fields from runtime sources; Pyright sees __init__.
    return Settings()  # pyright: ignore[reportCallIssue]
