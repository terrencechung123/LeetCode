class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashmap = {}
        for i, num in enumerate(nums):
            if nums[i] not in hashmap:
                hashmap[num]=1
            else:
                hashmap[num]+=1
        for x in hashmap:
            if hashmap[x] == 1:
                return x
        