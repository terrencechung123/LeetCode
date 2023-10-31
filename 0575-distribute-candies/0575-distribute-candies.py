class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        eat = int(len(candyType)/2)
        hashMap = {}
        for i, val in enumerate(candyType):
            if val not in hashMap:
                hashMap[val] = 1
            else:
                hashMap[val] +=1
        output = 0
        if len(hashMap) > eat:
            output = eat
        else:
            output = len(hashMap)

        return output