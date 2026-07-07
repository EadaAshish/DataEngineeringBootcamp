import logging

from logging_config import configure_logging

configure_logging()

logger = logging.getLogger(__name__)

logger.info("Application Started")