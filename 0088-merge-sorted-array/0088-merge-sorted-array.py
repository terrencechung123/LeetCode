class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        new_num = []
        new_num = [nums1[i] for i in range(m)]
        new_num += [nums2[i] for i in range(n)]
        new_num=sorted(new_num)
        
        nums1.clear()
        nums1.extend(new_num)