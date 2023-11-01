class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        empty = [0] + flowerbed + [0]
        count = 0
        for i in range(1,len(empty)-1):
            if empty[i] == 0 and empty[i-1] == 0 and empty[i+1] == 0:
                empty[i] = 1
                count+=1
        return count >= n