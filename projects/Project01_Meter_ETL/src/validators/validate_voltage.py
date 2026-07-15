import pandas as pd
from models import ValidationError, ValidationResult

MIN_VOLTAGE = 400
MAX_VOLTAGE = 450

def validate_voltage(df: pd.DataFrame) -> list[ValidationError]:
    
    meter_id_invalid_mask = (
        (df["voltage"].isna()) | (df["voltage"] < MIN_VOLTAGE) | (df["voltage"] > MAX_VOLTAGE)
    )

    errors: list[ValidationError] = []

    invalid_df = df[meter_id_invalid_mask].copy()

    for index, row in invalid_df.iterrows():
        errors.append(
            ValidationError(
                row=index,
                column="voltage",
                value=row["voltage"],
                message="Voltage must be between 400 and 450"
            )
        )

    return errors