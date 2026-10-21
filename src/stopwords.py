from nltk.corpus import stopwords

STOPWORDS = set(stopwords.words("english"))


def remove_stopwords(words: list[str]) -> list[str]:
    # Returner bare ordene som IKKE står i STOPWORDS
    pass
