class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        arr= ''
        for word in words:
            good = True
            for i in range(len(word)):
                if (word[i] not in chars) or word.count(word[i]) > chars.count(word[i]):
                    good = False
            if good:
                arr+=word
        return len(arr)