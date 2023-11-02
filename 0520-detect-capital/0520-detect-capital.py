class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.islower() == True or word.isupper() == True or (word[0].isupper() == True and word[1:].islower() == True)
