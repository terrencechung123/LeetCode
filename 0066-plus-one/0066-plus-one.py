class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        string = ''.join(str(digit) for digit in digits)
        value = int(string)+1
        value_string = str(value)
        result = [int(i) for i in value_string]
        return result