class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashMap = {}
        for i, val in enumerate(nums):
            diff = target - val
            if diff in hashMap:
                return [hashMap[diff], i]
            hashMap[val] = i
            