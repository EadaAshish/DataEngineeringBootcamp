import pandas as pd

from models import ValidationResult
from models import validation_error, ValidationError

def validate_dataframe(df: pd.DataFrame) -> ValidationError:

    return validation_error.validate_meter_id(df)