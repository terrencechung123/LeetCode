class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        new_nums = []
        count = 0
        for i in range(len(nums)):
            if nums[i] == val:
                count+=1
            else:
                new_nums.append(nums[i])
        nums.clear()
        nums.extend(new_nums)
        nums.extend([None] * count)

        return len(new_nums)