class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        hashSet = set(jewels)
        count=0
        for stone in stones:
            if stone in hashSet:
                count+=1
        return count