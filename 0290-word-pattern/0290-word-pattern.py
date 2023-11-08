class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word = s.split()
        charToWord = {}
        wordToChar = {}
        if len(pattern) != len(word):
            return False
        for c,w in zip(pattern, word):
            if c in charToWord and charToWord[c] != w:
                return False
            if w in wordToChar and wordToChar[w] != c:
                return False
            charToWord[c] = w
            wordToChar[w] = c
        return True