from collections import Counter


class AnagramTester:
    def __init__(self, word: str):
        self.word = word.lower()
        self.letters = Counter(self.word)

    def is_anagram_of(self, word: str):
        word_lower = word.lower()

        if self.word == word_lower:
            return False

        orig_set = self.letters.copy()
        for c in word.lower():
            if c in orig_set:
                orig_set[c] -= 1
                if orig_set[c] == 0:
                    orig_set.pop(c)
            else:
                return False
        return len(orig_set) == 0


def find_anagrams(word, candidates):
    tester = AnagramTester(word)
    return [c for c in candidates if tester.is_anagram_of(c)]
