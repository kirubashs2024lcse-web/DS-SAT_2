
import pandas as pd
from pathlib import Path


BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_DIR.mkdir(exist_ok=True)


trips = pd.read_csv(DATA_DIR / "trips.csv")
boardings = pd.read_csv(DATA_DIR / "boardings.csv")
routes = pd.read_csv(DATA_DIR / "routes.csv")
calendar = pd.read_csv(DATA_DIR / "calendar.csv")
operations = pd.read_csv(DATA_DIR / "operations.csv")

print("DATA CLEANING STARTED")

before = len(boardings)
boardings = boardings.drop_duplicates()
print("Duplicate boarding rows removed:", before - len(boardings))


for df in [trips, routes]:
    if "route" in df.columns:
        df["route"] = (
            df["route"]
            .astype("string")
            .str.strip()
            .str.replace(r"\s+", " ", regex=True)
            .str.title()
        )


for col in ["boarding", "alighting"]:
    boardings[col] = pd.to_numeric(
        boardings[col], errors="coerce"
    )

for col in ["boarding", "alighting"]:
    boardings.loc[boardings[col] < 0, col] = pd.NA


boardings["stop_id_missing"] = boardings["stop_id"].isna()

trips["date"] = pd.to_datetime(trips["date"], errors="coerce")
calendar["date"] = pd.to_datetime(calendar["date"], errors="coerce")


operations["delay_minutes"] = pd.to_numeric(
    operations["delay_minutes"], errors="coerce"
)


cleaned = {
    "trips_cleaned.csv": trips,
    "boardings_cleaned.csv": boardings,
    "routes_cleaned.csv": routes,
    "calendar_cleaned.csv": calendar,
    "operations_cleaned.csv": operations
}

for filename, df in cleaned.items():
    df.to_csv(OUTPUT_DIR / filename, index=False)

print("\nCLEANING SUMMARY")

for name, df in cleaned.items():
    print(f"\n{name}")
    print("Rows:", len(df))
    print("Missing values:")
    print(df.isna().sum())

print("\nCleaned files saved in:", OUTPUT_DIR)
print("DATA CLEANING COMPLETED")

