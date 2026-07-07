import logging  
from pathlib import Path

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    handlers=[
        logging.FileHandler(LOG_DIR / "application.log"),
        logging.StreamHandler()
    ]
)

logging_config = logging.getLogger(__name__)

logging_config.info("Logger initialized successfully.")