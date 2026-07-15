import pandas as pd
from models import ValidationError

def validate_meter_id(df: pd.DataFrame) -> list[ValidationError]:

    meter_id_invalid_mask = (
       (df["meter_id"].isna()) | (df["meter_id"].str.strip() == "")
    )

    errors: list[ValidationError] = []

    invalid_df = df[meter_id_invalid_mask].copy()

    for index, row in invalid_df.iterrows():
        errors.append(
            ValidationError(
                row=index,
                column="meter_id",
                value=row["meter_id"],
                message = 'Meter ID is missing'
            )
        )
    
    return errors