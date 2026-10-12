
import pandas as pd
from pathlib import Path

DATA_DIR = Path("data")


trips = pd.read_csv(DATA_DIR / "trips.csv")
boardings = pd.read_csv(DATA_DIR / "boardings.csv")
routes = pd.read_csv(DATA_DIR / "routes.csv")
calendar = pd.read_csv(DATA_DIR / "calendar.csv")
operations = pd.read_csv(DATA_DIR / "operations.csv")

datasets = {
    "Trips": trips,
    "Boardings": boardings,
    "Routes": routes,
    "Calendar": calendar,
    "Operations": operations
}

for name, df in datasets.items():
    print(f"\n{'=' * 45}")
    print(f"{name} Dataset")
    print(f"{'=' * 45}")
    print("Number of rows:", df.shape[0])
    print("Number of columns:", df.shape[1])
    print("\nFirst 5 rows:")
    print(df.head())
    print("\nColumn names:")
    print(df.columns.tolist())
    print("\nData types:")
    print(df.dtypes)
