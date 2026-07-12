import pandas as pd

from models import ValidationResult

def validate_dataframe(df: pd.DataFrame) -> ValidationResult:
    return ValidationResult(
        valid_dataframe=df,
        invalid_dataframe=pd.DataFrame(),
        errors=[],
        warnings=[]
    )