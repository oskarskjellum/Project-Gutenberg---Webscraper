import logging
from pathlib import Path

import requests

logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

DEFAULT_BOOK_ID = 79690
GUTENBERG_URL_TEMPLATE = "https://www.gutenberg.org/ebooks/{id}.txt.utf-8"
DATA_DIR = Path("data/raw")


class BookFetchError(Exception):
    pass

def build_url(book_id: int) -> str:
    return GUTENBERG_URL_TEMPLATE.format(id=book_id)

def fetch_book(book_id: int, save_dir: Path = DATA_DIR, timeout: int = 10) -> str:
    url = build_url(book_id)

    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
    except requests.RequestException as exc:
        raise BookFetchError(f"Klarte ikke hente bok {book_id} fra {url}") from exc
    
    save_dir.mkdir(parents=True, exist_ok=True)
    save_path = save_dir / f"{book_id}.txt"
    save_path.write_text(response.text, encoding="utf-8")

    logger.info("Lagret %d tegn til %s", len(response.text), save_path)
    return response.text



def fetch_books(book_ids: list[int], save_dir: Path = DATA_DIR) -> dict[int, str]:
    results = {}
    for book_id in book_ids:
        try:
            results[book_id] = fetch_book(book_id, save_dir)
        except BookFetchError as exc:
            logger.warning(str(exc))
    return results


if __name__ == "__main__":
    fetch_book(DEFAULT_BOOK_ID)