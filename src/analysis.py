import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

WORD_PATTERN = re.compile(r"\b[a-zA-Z']+\b")


@dataclass
class AnalysisResult:
    top_words: list[tuple[str, int]]
    hapax_legomena: list[str]  # ord som kun forekommer én gang
    frequency_table: list[tuple[str, int]]

    @property
    def unique_word_count(self) -> int:
        return len(self.frequency_table)

    @property
    def total_word_count(self) -> int:
        return sum(count for _, count in self.frequency_table)


def tokenize(text: str) -> list[str]:
    return WORD_PATTERN.findall(text.lower())


def analyze_text(text: str, top_n: int = 3) -> AnalysisResult:
    counter = Counter(tokenize(text))
    frequency_table = counter.most_common()

    return AnalysisResult(
        top_words=frequency_table[:top_n],
        hapax_legomena=[word for word, count in counter.items() if count == 1],
        frequency_table=frequency_table,
    )


def load_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def print_summary(result: AnalysisResult, preview: int = 10) -> None:
    print(f"Unike ord: {result.unique_word_count}")
    print(f"Totalt antall ord: {result.total_word_count}")

    print(f"\nTopp {len(result.top_words)} mest brukte ord:")
    for word, count in result.top_words:
        print(f"  {word:<15} {count}")

    print(f"\nOrd brukt kun én gang: {len(result.hapax_legomena)}")

    print(f"\nFrekvenstabell (topp {preview}):")
    for word, count in result.frequency_table[:preview]:
        print(f"  {word:<15} {count}")


if __name__ == "__main__":
    text = load_text(Path("data/raw/2701.txt"))
    result = analyze_text(text, top_n=3)
    print_summary(result)
   
