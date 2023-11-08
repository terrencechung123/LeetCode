class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count=0
        arr = []
        for num in nums:
            if num != val:
                count+=1
                arr.append(num)
        nums.clear()
        nums.extend(arr)
        for i in range(count):
            nums.append(0)

        return count