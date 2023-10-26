class Solution:
    def missingNumber(self, n: List[int]) -> int:
        mySet=set()
        for i in range(len(n)+1):
            mySet.add(i)
        for x in mySet:
            if x not in n:
                return x