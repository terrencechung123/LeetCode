class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for num in nums1:
            greater = False
            for i in range(nums2.index(num)+1,len(nums2)):
                if nums2[i] > num:
                    result.append(nums2[i])
                    greater = True
                    break
            if not greater:
                result.append(-1)

        return result