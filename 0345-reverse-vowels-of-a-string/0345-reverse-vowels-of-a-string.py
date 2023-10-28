class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a','e','i','o','u','A','E','I','O','U'}
        s_vowels = [] #[e,e,o,e]
        for i in range(len(s)):
            if s[i] in vowels:
                s_vowels.append(s[i])
        new_s = list(s)
        for i in range(len(new_s)):
            if new_s[i] in vowels:
                new_s[i] = s_vowels[-1]
                s_vowels.pop()
        new_s = ''.join(new_s)
        return new_s