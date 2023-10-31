class Solution:
    def calPoints(self, ops: List[str]) -> int:
        hashSet = {'C','D','+'}
        arr = []
        for op in ops:
            if op not in hashSet:
                arr.append(op)

            else:
                if op == 'C':
                    arr.pop()

                if op == 'D':
                    arr.append(str(int(arr[-1])*2))
                if op == '+':
                    arr.append(int(arr[-1])+int(arr[-2]))
        return sum([int(i) for i in arr])