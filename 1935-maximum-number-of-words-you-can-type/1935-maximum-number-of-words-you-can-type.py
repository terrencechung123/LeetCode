class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text = text.split()
        cantType = []
        for word in text:
            for char in word:
                if char in brokenLetters:
                    cantType.append(word)
                    break
        return len(text) - len(cantType)