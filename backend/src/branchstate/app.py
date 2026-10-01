"""Minimal HTTP application; independent of persistence and simulation."""

from typing import Literal

from fastapi import FastAPI
from pydantic import BaseModel

from branchstate.settings import load_settings


class HealthResponse(BaseModel):
    status: Literal["ok"]


def create_app() -> FastAPI:
    settings = load_settings()
    application = FastAPI(title=settings.app_name, version="0.1.0")

    @application.get("/health", response_model=HealthResponse, operation_id="getHealth")
    def health() -> HealthResponse:
        return HealthResponse(status="ok")

    return application
