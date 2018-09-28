from collections import Counter
import re


def word_count(phrase: str):
    return Counter(
        [w.strip("'") for w in re.findall(r"[a-z0-9']+", phrase.lower())]
    )