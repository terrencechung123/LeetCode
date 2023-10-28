class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        new_list=[]
        for num in nums:
            new_list.append(num**2)
        return sorted(new_list)