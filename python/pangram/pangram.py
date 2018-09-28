def is_pangram(sentence: str):
    unique_letters = set()
    for c in sentence:
        if c.isalpha():
            unique_letters.add(c.lower())
    return len(unique_letters) == 26
