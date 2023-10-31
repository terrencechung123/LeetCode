class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        new_num = sorted([nums1[i] for i in range(m)] + [nums2[i] for i in range(n)])
        nums1.clear()
        nums1.extend(new_num)