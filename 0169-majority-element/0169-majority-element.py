class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]] =1
            else:
                hashmap[nums[i]]= hashmap[nums[i]]+1
        for num, value in hashmap.items():
            if value > len(nums)/2:
                return num