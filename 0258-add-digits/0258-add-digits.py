class Solution:
    def addDigits(self, num: int) -> int:
        new_num = str(num)
        sum = 0
        while True:
            for i in range(len(new_num)):
                sum += int(new_num[i])
            if sum < 10:
                break
            new_num = str(sum)
            sum=0
        return sum