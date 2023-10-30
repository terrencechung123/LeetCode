class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        new_s, new_t = sorted(s), sorted(t)
        for i in range(len(new_t)):
            if i >= len(new_s) or new_t[i] != new_s[i]:
                return new_t[i]