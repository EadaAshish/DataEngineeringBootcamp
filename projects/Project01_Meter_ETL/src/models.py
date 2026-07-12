from dataclasses import dataclass
import pandas as pd

@dataclass
class ValidationResult:
    valid_dataframe: pd.DataFrame
    invalid_dataframe: pd.DataFrame
    errors: list[str]
    warnings: list[str]