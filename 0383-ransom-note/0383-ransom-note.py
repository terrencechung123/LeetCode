class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap = {}
        for i in magazine:
            if i in hashmap:
                hashmap[i] +=1
            else:
                hashmap[i] = 1
        for i in ransomNote:
            if i not in hashmap:
                return False
            else:
                hashmap[i] -= 1
        for i in hashmap:
            if hashmap[i] < 0:
                return False
        return True