class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        y=''
        for i in range(len(str_x)):
            y = str_x[i] + y
        return y == str_x