class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        hashset = set()
        new_nums = []
        for i in range(len(nums)):
            if nums[i] not in hashset:
                hashset.add(nums[i])
                new_nums.append(nums[i])
        nums.clear()
        nums.extend(new_nums)
        return len(hashset)