class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        count = 1
        while True:
            if count % 2 == 0 and count % n == 0:
                return count
            count+=1