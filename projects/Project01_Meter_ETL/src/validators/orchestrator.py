import pandas as pd
from models.validation_result import ValidationResult, ValidationError
from .validate_meter_id import validate_meter_id
from .validate_voltage import validate_voltage

def validate_dataframe(df: pd.DataFrame) -> ValidationResult:
    
    validators = [
        validate_meter_id,
        validate_voltage
    ]

    errors: list[ValidationError] = []

    for validation in validators:
        errors.extend(validation(df))

    rows_with_errors = set()

    for error in errors:
        rows_with_errors.add(error.row)

    invalid_mask = df.index.isin(rows_with_errors)

    invalid_df = df.loc[invalid_mask].copy()
    valid_df = df.loc[~invalid_mask].copy()
    

    return ValidationResult(
        valid_dataframe=valid_df,
        invalid_dataframe=invalid_df,
        errors=errors,
        warnings=[]
    )