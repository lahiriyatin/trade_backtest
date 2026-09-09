from pathlib import Path
from zoneinfo import ZoneInfo

PROJECT_ROOT = Path(__file__).resolve().parent.parent


DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
RESULTS_DIR = PROJECT_ROOT / "results"
LOG_DIR = PROJECT_ROOT / "logs"

SOURCE_TIME = ZoneInfo("UTC")
SESSION_TIME = ZoneInfo("America/New_York")

TWELVE_DATA_BASE_URL = "https://api.twelvedata.com"

DEFAULT_INTERVAL = "1min"
DEFAULT_OUTPUT_SIZE = 100

REQUEST_TIMEOUT_SECONDS = 30