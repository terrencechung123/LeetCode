class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num_str = ''.join(str(num) for num in digits)
        new_num = int(num_str)+1
        str_new_num = str(new_num)
        new_number = [int(i) for i in str_new_num]
        result = new_number
        return result