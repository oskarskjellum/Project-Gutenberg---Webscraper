import logging
from pathlib import Path

import requests

logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

DEFAULT_BOOK_ID = 79690
gutenberg_base_url = "https://www.gutenberg.org/ebooks/79690"
data_dir = Path("data/raw")
