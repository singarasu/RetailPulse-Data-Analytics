import pandas as pd
from pathlib import Path

# Raw dataset folder
data_path = Path("data/raw")

# Read all CSV files
csv_files = list(data_path.glob("*.csv"))

print(f"Total CSV files found: {len(csv_files)}\n")

for file in csv_files:
    df = pd.read_csv(file)

    print("=" * 70)
    print(f"File: {file.name}")
    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")
    print("\nColumn Names:")
    print(list(df.columns))

    print("\nMissing Values:")
    print(df.isnull().sum().sum())

    print(f"Duplicate Rows: {df.duplicated().sum()}")