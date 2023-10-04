class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        string = str(x)
        reversed_string = ''
        for i in range(len(string)):
            reversed_string += string[-1-i]
        if string == reversed_string:
            return True
        else:
            return False