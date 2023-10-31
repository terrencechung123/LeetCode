class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for i in range(left,right+1):
            num_str = str(i)
            isTrue=True
            for digit in num_str:
                if int(digit) == 0 or i % int(digit) != 0:
                    isTrue=False
                    break
            if isTrue:
                result.append(i)

        return result