import logging
import pandas as pd
from extractor import extract_csv
from pathlib import Path
from logging_config import configure_logging
from models import ValidationResult

configure_logging()
logger = logging.getLogger(__name__)
logger.info("Application Started")

CSV_PATH = Path('data/input/meter_data.csv')

try:
    logger.info("Starting extraction.")
    df = extract_csv(CSV_PATH)
    logger.info(
        "Successfully extracted %d records from %s.",
        len(df),
        CSV_PATH.name
    )
except FileNotFoundError:
    logger.exception("Input file not found: %s", CSV_PATH)
    raise
except Exception:
    logger.exception("Unexpected error during extraction.")
    raise

print(df.info())

result = ValidationResult(
    valid_dataframe=df,
    invalid_dataframe=pd.DataFrame(),
    errors=[],
    warnings=[]
)

print(result)