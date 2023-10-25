class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string = ''
        for i in range(len(s)):
            if s[i].isalnum():
                new_string += s[i]
        new_string = new_string.lower()
        reversed_string = ''
        for j in range(len(new_string)):
            reversed_string += new_string[-1-j]
        if reversed_string == new_string:
            return True
        return False