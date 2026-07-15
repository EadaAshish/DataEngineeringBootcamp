from pathlib import Path
import logging

from extractors import extract_csv
from validators import validate_dataframe
from utils import configure_logging

configure_logging()

logger = logging.getLogger(__name__)

CSV_PATH = Path("data/input/meter_data.csv")

df = extract_csv(CSV_PATH)

validation_result = validate_dataframe(df)

print(validation_result.errors)