# SPDX-License-Identifier: MIT
"""Verify PostgreSQL in a disposable Compose project; remove only its test data."""

import os
from pathlib import Path
import secrets
import socket
import subprocess
import tempfile
import uuid


ROOT = Path(__file__).resolve().parents[1]


def verify() -> None:
    project = f"branchstate-check-{uuid.uuid4().hex[:12]}"
    password = secrets.token_urlsafe(32)
    environment = os.environ.copy()
    for name in list(environment):
        if name.startswith(("POSTGRES_", "COMPOSE_")):
            del environment[name]

    def run(command, *, sql=None, check=True):
        result = subprocess.run(
            command, cwd=ROOT, env=environment, input=sql,
            capture_output=True, text=True, timeout=300,
        )
        if check and result.returncode:
            detail = (result.stdout + result.stderr).replace(password, "[redacted]")
            raise RuntimeError(detail.strip())
        return result

    # Refuse to reuse any resources, even in the unlikely event of a name collision.
    label = f"label=com.docker.compose.project={project}"
    for kind in ("container", "volume", "network"):
        existing = run(["docker", kind, "ls", "--filter", label, "--quiet"])
        if existing.stdout.strip():
            raise RuntimeError(f"Refusing to reuse existing {kind} resources")

    with socket.socket() as port_probe:
        port_probe.bind(("127.0.0.1", 0))
        port = port_probe.getsockname()[1]

    with tempfile.TemporaryDirectory(prefix="branchstate-postgres-") as directory:
        settings = Path(directory) / ".env"
        settings.write_text(
            f"POSTGRES_PASSWORD={password}\nPOSTGRES_USER=branchstate\n"
            f"POSTGRES_DB=branchstate\nPOSTGRES_PORT={port}\n"
        )
        settings.chmod(0o600)
        compose = [
            "docker", "compose", "--project-name", project,
            "--env-file", str(settings), "--file", str(ROOT / "compose.yaml"),
        ]

        def up():
            run(compose + ["up", "--detach", "--wait", "--wait-timeout", "90", "db"])

        def query(sql, *, wrong_password=False, check=True):
            assignment = (
                "PGPASSWORD=deliberately-invalid-password" if wrong_password
                else 'PGPASSWORD="$POSTGRES_PASSWORD"'
            )
            return run(compose + [
                "exec", "--no-TTY", "db", "sh", "-ec",
                f"export {assignment}; "
                'exec psql --host=127.0.0.1 --username="$POSTGRES_USER" '
                '--dbname="$POSTGRES_DB" --no-password --no-psqlrc '
                '--set=ON_ERROR_STOP=1 --tuples-only --no-align',
            ], sql=sql, check=check)

        missing = Path(directory) / "missing.env"
        missing.write_text("POSTGRES_PASSWORD=\n")
        rejected = run([
            "docker", "compose", "--project-name", project,
            "--env-file", str(missing), "--file", str(ROOT / "compose.yaml"),
            "config", "--quiet",
        ], check=False)
        if rejected.returncode == 0 or "POSTGRES_PASSWORD" not in rejected.stderr:
            raise RuntimeError("Compose accepted an empty database password")
        print("PASS: missing password rejected", flush=True)

        try:
            up()
            with socket.create_connection(("127.0.0.1", port), timeout=5):
                pass
            if query("SHOW server_version_num;\n").stdout.strip() != "180006":
                raise RuntimeError("Expected PostgreSQL 18.6")
            print("PASS: healthy PostgreSQL 18.6, published loopback port and authenticated SQL", flush=True)

            rejected = query("SELECT 1;\n", wrong_password=True, check=False)
            if rejected.returncode == 0 or "password authentication failed" not in rejected.stderr:
                raise RuntimeError("Incorrect password was not rejected by TCP authentication")
            print("PASS: incorrect password rejected", flush=True)

            query(
                "CREATE TABLE compose_verification (value text NOT NULL);\n"
                "INSERT INTO compose_verification VALUES ('persisted');\n"
            )
            for action in ("restart", "recreate"):
                if action == "restart":
                    run(compose + ["restart", "db"])
                else:
                    run(compose + ["down"])
                up()
                if query("SELECT value FROM compose_verification;\n").stdout.strip() != "persisted":
                    raise RuntimeError(f"Data lost after {action}")
                print(f"PASS: data persists after {action}", flush=True)
        finally:
            # Only this fresh random project's disposable data is destroyed.
            run(compose + ["down", "--volumes"])
            print("Removed disposable verification containers, network and volume", flush=True)


if __name__ == "__main__":
    try:
        verify()
    except (RuntimeError, subprocess.TimeoutExpired, OSError) as error:
        raise SystemExit(f"PostgreSQL verification failed: {error}") from None
