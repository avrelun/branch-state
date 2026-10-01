import os
import tomllib
from pathlib import Path

import pytest
from pydantic import ValidationError

from branchstate.settings import Settings, load_settings


@pytest.fixture
def config_dir(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    for name in tuple(os.environ):
        if name.upper().startswith("BRANCHSTATE_"):
            monkeypatch.delenv(name)
    monkeypatch.setenv("BRANCHSTATE_CONFIG_DIR", str(tmp_path))
    (tmp_path / "config.toml").write_text(
        'app_name = "Branchstate"\n', encoding="utf-8"
    )
    return tmp_path


def test_sources_follow_priority_without_caching(
    config_dir: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    config_file = config_dir / "config.toml"
    dotenv_file = config_dir / ".env"
    config_file.write_text(
        'app_name = "from-toml"\nenvironment = "production"\n', encoding="utf-8"
    )
    dotenv_file.write_text(
        "BRANCHSTATE_APP_NAME=from-dotenv\nBRANCHSTATE_ENVIRONMENT=test\n",
        encoding="utf-8",
    )
    monkeypatch.setenv("BRANCHSTATE_APP_NAME", "from-process")
    monkeypatch.setenv("BRANCHSTATE_ENVIRONMENT", "development")

    settings = load_settings()
    assert (settings.app_name, settings.environment) == ("from-process", "development")

    monkeypatch.delenv("BRANCHSTATE_APP_NAME")
    monkeypatch.delenv("BRANCHSTATE_ENVIRONMENT")
    settings = load_settings()
    assert (settings.app_name, settings.environment) == ("from-dotenv", "test")

    dotenv_file.unlink()
    settings = load_settings()
    assert (settings.app_name, settings.environment) == ("from-toml", "production")

    config_file.write_text('app_name = "from-toml"\n', encoding="utf-8")
    assert load_settings().environment == "development"


@pytest.mark.parametrize("value", ["", "   "])
def test_invalid_winning_environment_does_not_fall_back(
    config_dir: Path, monkeypatch: pytest.MonkeyPatch, value: str
) -> None:
    (config_dir / ".env").write_text(
        "BRANCHSTATE_APP_NAME=valid-dotenv\n", encoding="utf-8"
    )
    monkeypatch.setenv("BRANCHSTATE_APP_NAME", value)

    with pytest.raises(ValidationError) as error:
        load_settings()
    assert error.value.errors()[0]["loc"] == ("app_name",)


def test_unknown_environment_value_is_rejected(
    config_dir: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setenv("BRANCHSTATE_ENVIRONMENT", "staging")

    with pytest.raises(ValidationError) as error:
        load_settings()
    assert error.value.errors()[0]["type"] == "literal_error"


def test_missing_required_app_name_is_rejected(config_dir: Path) -> None:
    (config_dir / "config.toml").unlink()

    with pytest.raises(ValidationError) as error:
        load_settings()
    assert error.value.errors()[0]["type"] == "missing"
    assert error.value.errors()[0]["loc"] == ("app_name",)


@pytest.mark.parametrize(
    ("filename", "content"),
    [
        ("config.toml", 'app_name = "Branchstate"\nunknown = "unexpected"\n'),
        (".env", "BRANCHSTATE_UNKNOWN=unexpected\n"),
        (".env", "UNRELATED_KEY=unexpected\n"),
        (".env", "BRANCHSTATE_UNKNOWN=\n"),
        (".env", "BRANCHSTATE_UNKNOWN\n"),
        (".env", "UNRELATED_KEY=\n"),
        (".env", "UNRELATED_KEY\n"),
    ],
)
def test_unknown_file_keys_are_rejected(
    config_dir: Path, filename: str, content: str
) -> None:
    (config_dir / filename).write_text(content, encoding="utf-8")

    with pytest.raises(ValidationError) as error:
        load_settings()
    assert error.value.errors()[0]["type"] == "extra_forbidden"


def test_empty_declared_dotenv_value_is_validated(
    config_dir: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    (config_dir / ".env").write_text("BRANCHSTATE_APP_NAME=\n", encoding="utf-8")

    with pytest.raises(ValidationError) as error:
        load_settings()
    assert error.value.errors()[0]["type"] == "string_too_short"

    monkeypatch.setenv("BRANCHSTATE_APP_NAME", "valid-process")
    assert load_settings().app_name == "valid-process"


def test_malformed_toml_is_not_hidden_by_environment(
    config_dir: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    (config_dir / "config.toml").write_text("app_name = [\n", encoding="utf-8")
    monkeypatch.setenv("BRANCHSTATE_APP_NAME", "valid-process")

    with pytest.raises(tomllib.TOMLDecodeError):
        load_settings()


def test_constructor_values_are_not_a_configuration_source(config_dir: Path) -> None:
    settings = Settings(app_name="from-constructor", environment="test")

    assert settings.app_name == "Branchstate"
    assert settings.environment == "development"


def test_explicit_config_directory_is_independent_of_cwd(
    config_dir: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    other_directory = config_dir / "unrelated"
    other_directory.mkdir()
    (other_directory / "config.toml").write_text(
        'app_name = "wrong-directory"\n', encoding="utf-8"
    )
    monkeypatch.chdir(other_directory)

    assert load_settings().app_name == "Branchstate"


def test_editable_default_directory_is_independent_of_cwd(
    config_dir: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.delenv("BRANCHSTATE_CONFIG_DIR")
    monkeypatch.chdir(config_dir)
    (config_dir / "config.toml").write_text(
        'app_name = "wrong-directory"\n', encoding="utf-8"
    )

    assert load_settings().app_name == "Branchstate"


@pytest.mark.parametrize("directory", ["", "relative", "missing", "file"])
def test_explicit_config_directory_must_exist_and_be_absolute(
    config_dir: Path, monkeypatch: pytest.MonkeyPatch, directory: str
) -> None:
    if directory == "missing":
        value = str(config_dir / "missing")
    elif directory == "file":
        value = str(config_dir / "config.toml")
    else:
        value = directory
    monkeypatch.setenv("BRANCHSTATE_CONFIG_DIR", value)

    with pytest.raises(ValueError, match="BRANCHSTATE_CONFIG_DIR"):
        load_settings()
