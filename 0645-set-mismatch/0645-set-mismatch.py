class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        mySet = set()
        arr = []
        for num in nums:
            if num not in mySet:
                mySet.add(num)
            else:
                arr.append(num)
        for i in range(1,len(nums)+1):
            if i not in mySet:
                arr.append(i)
        return arr