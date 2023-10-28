class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        new_list = []
        for i in range(len(s)-1,-1,-1):
            new_list.append(s[i])
        s.clear()
        s.extend(new_list)