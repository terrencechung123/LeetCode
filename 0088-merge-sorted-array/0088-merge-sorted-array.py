class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        new_list = []
        for i in range(m):
            new_list.append(nums1[i])
        for i in range(n):
            new_list.append(nums2[i])
        new_list = sorted(new_list)
        nums1.clear()
        nums1.extend(new_list)
        return nums1