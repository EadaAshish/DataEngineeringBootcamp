from dataclasses import dataclass
import pandas as pd
from .validation_error import ValidationError

@dataclass
class ValidationResult:
    valid_dataframe: pd.DataFrame
    invalid_dataframe: pd.DataFrame
    errors: list[ValidationError]
    warnings: list[str]

### USE DataClass Instead of This

# class ValidationResult:

#     valid_dataframe: pd.DataFrame
#     invalid_dataframe: pd.DataFrame
#     errors: list[str]
#     warnings: list[str]

#     def __init__(
#         self,
#         valid_dataframe: pd.DataFrame,
#         invalid_dataframe: pd.DataFrame,
#         errors: list[str],
#         warnings: list[str]
#     ):
#         self.valid_dataframe = valid_dataframe
#         self.invalid_dataframe = invalid_dataframe
#         self.errors = errors
#         self.warnings = warnings