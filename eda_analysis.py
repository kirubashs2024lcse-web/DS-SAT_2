
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

BASE_DIR = Path(__file__).parent
OUTPUT_DIR = BASE_DIR / "output"
GRAPH_DIR = OUTPUT_DIR / "graphs"
GRAPH_DIR.mkdir(parents=True, exist_ok=True)

# Load datasets first
trips = pd.read_csv(OUTPUT_DIR / "trips_cleaned.csv")
boardings = pd.read_csv(OUTPUT_DIR / "boardings_cleaned.csv")
operations = pd.read_csv(OUTPUT_DIR / "operations_cleaned.csv")
calendar = pd.read_csv(OUTPUT_DIR / "calendar_cleaned.csv")

# Convert dates after loading
trips["date"] = pd.to_datetime(trips["date"], errors="coerce")
calendar["date"] = pd.to_datetime(calendar["date"], errors="coerce")
