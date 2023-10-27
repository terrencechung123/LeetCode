class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        maxNum = max(nums)
        minNum = min(nums)
        for i in range(len(nums)+1):
            if i not in nums or i == len(nums):
                return i