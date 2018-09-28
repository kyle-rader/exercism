from collections import defaultdict

def is_isogram(input: str):
    unique_chars = set()
    for c in input.lower():
        if c == " " or c == "-":
            continue
        if c in unique_chars:
            return False
        unique_chars.add(c)
    return True
