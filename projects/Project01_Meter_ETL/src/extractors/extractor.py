from pathlib import Path
import pandas as pd

def extract_csv(file_path: str | Path) -> pd.DataFrame:
    return pd.read_csv(file_path)

