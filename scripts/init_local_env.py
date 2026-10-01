# SPDX-License-Identifier: MIT
"""Create private local Compose settings without overwriting an existing file."""

import os
from pathlib import Path
import secrets


def create_env(destination: Path, template: Path) -> None:
    content = template.read_text()
    if content.count("POSTGRES_PASSWORD=\n") != 1:
        raise ValueError("Expected one empty POSTGRES_PASSWORD in .env.example")
    content = content.replace(
        "POSTGRES_PASSWORD=\n", f"POSTGRES_PASSWORD={secrets.token_urlsafe(32)}\n"
    )
    descriptor = os.open(destination, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    with os.fdopen(descriptor, "w") as output:
        output.write(content)


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    try:
        create_env(root / ".env", root / ".env.example")
    except FileExistsError:
        raise SystemExit(".env already exists; preserved without changes.") from None
    print("Created private .env with a generated password; adjust POSTGRES_PORT if needed.")
