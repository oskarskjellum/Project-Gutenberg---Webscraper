import logging
from pathlib import Path

import requests

logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

DEFAULT_BOOK_ID = 79690
gutenberg_url_template = "https://www.gutenberg.org/cache/epub/{book_id}/pg{book_id}.txt"
data_dir = Path("data/raw")


class bookFetchError(Exception):
    pass

def build_url(book_id: int) -> str:
    return guttenberg_url_template.format(book_id=book_id)

def fetch_book(book_id: int, save_dir: Path = data_dir, timeout: int = 10) -> str:
    url = build_url(book_id)
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
    except requests.RequestException as exc:
        raise bookFetchError(f"Could not fetch book {book_id} from {url}") from exc

    text = response.text
    save_dir.mkdir(parents=True, exist_ok=True)
    (save_dir / f"{book_id}.txt").write_text(text, encoding="utf-8")
    logger.info("Saved book %s to %s", book_id, save_dir / f"{book_id}.txt")
    return text

def fetch_book(book_ids:list[int], save_dir: Path = DATA_DIR) -> dict [int, str] 
     results = {}
     for book_id in book_ids:
         try:
             results[book_id] = fetch_book(book_id, save_dir)
         except BookFetchError as exc:
             logger.warning(str(exc))
      return results


if __name__ == "__main__":
    fetch_book([DEFAULT_BOOK_ID])
    
