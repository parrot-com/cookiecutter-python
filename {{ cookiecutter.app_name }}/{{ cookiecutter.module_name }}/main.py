import time

import prometheus_client

from {{ cookiecutter.module_name }}.config import settings
from {{ cookiecutter.module_name }}.logging import configure_logging
from {{ cookiecutter.module_name }}.logging import get_logger
from {{ cookiecutter.module_name }}.metrics import TICKS

configure_logging()

logger = get_logger(__name__)


def run():
    if settings.prometheus_enabled:
        prometheus_client.start_http_server(settings.prometheus_port)

    while True:
        logger.info("tick")

        TICKS.inc()

        time.sleep(1)
