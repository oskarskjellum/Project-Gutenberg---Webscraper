import pytest

from src.analysis import analyze_text, tokenize

SAMPLE_TEXT = "Katten satt på matten. Katten løp bort!"


@pytest.fixture
def result():
    return analyze_text(SAMPLE_TEXT, top_n=2)


def test_tokenize_strips_punctuation_and_lowercases():
    assert tokenize("Katt, katt! KATT.") == ["katt", "katt", "katt"]


def test_top_words(result):
    assert result.top_words == [("katten", 2), ("satt", 1)]


def test_hapax_legomena(result):
    assert set(result.hapax_legomena) == {"satt", "på", "matten", "løp", "bort"}


def test_frequency_table_is_sorted_descending(result):
    counts = [count for _, count in result.frequency_table]
    assert counts == sorted(counts, reverse=True)


def test_word_counts(result):
    assert result.total_word_count == 7
    assert result.unique_word_count == 6