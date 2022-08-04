import os
import functools
from typing import Literal, Optional

from pydantic import BaseSettings, HttpUrl

app_env = os.environ.get("APP_ENV", "dev")


@functools.lru_cache
class Settings(BaseSettings):
    app_name: str = "{{ cookiecutter.app_name }}"
    app_env: Literal["production", "staging", "dev", "test"] = "dev"
    release_version: Optional[str] = None
    log_level: Literal["CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG"] = "ERROR"

    # Sentry
    sentry_dsn: Optional[HttpUrl] = None

    # Prometheus
    prometheus_port: int = 8081

    class Config:
        env_file = ".env" if app_env == "dev" else f".env.{app_env}"


settings = Settings()
