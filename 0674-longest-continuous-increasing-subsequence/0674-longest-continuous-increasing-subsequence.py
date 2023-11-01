class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        count = 1
        current = 1
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                count+=1
            else:
                if count > current:
                    current = count
                count=1
        if count > current:
            return count
        return current