class Solution:
    def addDigits(self, num: int) -> int:
        new_num = str(num)
        while True:
            sum=0
            for i in range(len(new_num)):
                sum += int(new_num[i])
            if sum < 10:
                break
            new_num = str(sum)
        return sum