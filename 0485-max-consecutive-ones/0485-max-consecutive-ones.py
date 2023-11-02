class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        mySet = set()
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                mySet.add(count)
                count = 0
        mySet.add(count)
        return max(mySet)