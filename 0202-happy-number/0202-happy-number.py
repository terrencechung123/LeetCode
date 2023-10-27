class Solution:
    def isHappy(self, n: int) -> bool:
        str_num = ''.join(map(str,str(n)))
        sum=0
        for i in str_num:
            sum += int(i)**2
        hashset=set()
        while sum not in hashset:
            hashset.add(sum)
            new_sum = ''.join(map(str,str(sum)))
            sum = 0
            for i in new_sum:
                sum += int(i)**2
        if sum == 1:
            return True
        else:
            return False