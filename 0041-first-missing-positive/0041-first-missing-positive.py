class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        hashSet = set(nums)
        num_max = max(nums)
        if num_max < 0:
            return 1
        for i in range(1, num_max):
            if i not in hashSet:
                return i
        else:
            return num_max+1