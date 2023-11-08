class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr = []
        for i in range(len(nums)):
            count = 0
            for num in nums:
                if nums[i] != num and nums[i] > num:
                    count+=1
            arr.append(count)
        return arr