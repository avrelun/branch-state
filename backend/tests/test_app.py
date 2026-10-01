"""HTTP contract checks; no database or external server required."""

import os
from collections.abc import Iterator
from pathlib import Path

import pytest
from fastapi.testclient import TestClient
from pydantic import ValidationError

from branchstate.app import create_app


@pytest.fixture
def client(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> Iterator[TestClient]:
    for name in tuple(os.environ):
        if name.upper().startswith("BRANCHSTATE_"):
            monkeypatch.delenv(name)
    monkeypatch.setenv("BRANCHSTATE_CONFIG_DIR", str(tmp_path))
    monkeypatch.setenv("BRANCHSTATE_APP_NAME", "Branchstate test")
    with TestClient(create_app()) as test_client:
        yield test_client


def test_health_contract(client: TestClient) -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert response.json() == {"status": "ok"}


def test_unknown_route(client: TestClient) -> None:
    response = client.get("/missing")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}


def test_health_rejects_post(client: TestClient) -> None:
    response = client.post("/health")
    assert response.status_code == 405
    assert response.headers["allow"] == "GET"
    assert response.json() == {"detail": "Method Not Allowed"}


def test_openapi_contract(client: TestClient) -> None:
    schema = client.get("/openapi.json").json()
    operation = schema["paths"]["/health"]["get"]
    assert operation["operationId"] == "getHealth"
    assert operation["responses"]["200"]["content"]["application/json"]["schema"] == {
        "$ref": "#/components/schemas/HealthResponse"
    }
    assert schema["components"]["schemas"]["HealthResponse"]["required"] == ["status"]
    assert (
        schema["components"]["schemas"]["HealthResponse"]["properties"]["status"][
            "const"
        ]
        == "ok"
    )


def test_invalid_settings_prevent_app_creation(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    monkeypatch.setenv("BRANCHSTATE_CONFIG_DIR", str(tmp_path))
    monkeypatch.setenv("BRANCHSTATE_APP_NAME", "")
    with pytest.raises(ValidationError):
        create_app()
