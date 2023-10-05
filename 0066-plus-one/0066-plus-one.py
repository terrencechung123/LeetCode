class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num_str = ''.join(str(num) for num in digits)
        new_num = int(num_str)+1
        str_new_num = str(new_num)
        new_number = []
        for i in str_new_num:
            new_number.append(i)
        integers = [int(i) for i in new_number]


        result = integers
        return result