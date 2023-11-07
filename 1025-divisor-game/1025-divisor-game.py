class Solution:
    def divisorGame(self, n: int) -> bool:
        count = 0
        while True:
            move = False
            for i in range(1,n):
                if n % i == 0:
                    count+=1
                    n = n - i
                    move = True
                    break
            if move == False:
                break

        return count % 2 == 1