class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        new_list = []
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            new_list.append(total)
        return new_list
            