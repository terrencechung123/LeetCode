class Solution:
    def maxProfit(self, s: List[int]) -> int:
        l,r = 0,1
        profit = 0
        while r < len(s):
            if s[l] > s[r]:
                l=r
                r+=1
            else:
                diff = s[r]-s[l]
                if diff > profit:
                    profit = diff
                r+=1
        return profit
