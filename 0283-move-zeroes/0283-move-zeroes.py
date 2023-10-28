class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        new_nums = []
        count=[]
        for i in range(len(nums)):
            if nums[i] != 0:
                new_nums.append(nums[i])
            else:
                count.append(0)
        nums.clear()
        nums.extend(new_nums)
        nums.extend(count)