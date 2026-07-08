import logging
from extractor import extract_csv
from pathlib import Path
from logging_config import configure_logging

configure_logging()
logger = logging.getLogger(__name__)
logger.info("Application Started")

CSV_PATH = Path('data/input/meter_data.csv')
df = extract_csv(CSV_PATH)

logger.info(
    "Successfully extracted %d records from %s.",
    len(df),
    CSV_PATH.name
)

print(df.info())
