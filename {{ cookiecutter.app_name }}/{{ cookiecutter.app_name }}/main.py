import time

import prometheus_client

from {{ cookiecutter.app_name }}.config import settings
from {{ cookiecutter.app_name }}.logging import get_logger
from {{ cookiecutter.app_name }}.metrics import TICKS

logger = get_logger(__name__)


def run():
    prometheus_client.start_http_server(settings.prometheus_port)

    while True:
        logger.info("tick")

        TICKS.inc()

        time.sleep(1)
