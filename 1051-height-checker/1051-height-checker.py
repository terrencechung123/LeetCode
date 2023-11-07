class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        target = sorted(heights)
        hashSet=set()
        for i in range(len(heights)):
            if heights[i] !=  target[i]:
                hashSet.add(i)
        return len(hashSet)