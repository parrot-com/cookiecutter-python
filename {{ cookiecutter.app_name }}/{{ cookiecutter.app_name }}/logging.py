import logging

import sentry_sdk
from parrottools.logging import configure_logging as configure
from parrottools.logging import log_contex

from {{ cookiecutter.app_name }}.config import settings


def configure_logging() -> None:
    configure(
        level=settings.log_level,
        sentry_enabled=settings.sentry_dsn,
        service_name=settings.app_name,
        service_version=settings.release_version,
        deployment_env=settings.app_env,
    )

    if settings.sentry_dsn:
        sentry_sdk.init(
            dsn=settings.sentry_dsn,
            release=settings.release_version,
            environment=settings.app_env,
        )


def get_logger(logger_name: str) -> logging.Logger:
    return logging.getLogger(logger_name)

__all__ = ["configure_logging", "get_logger", "log_context"]
