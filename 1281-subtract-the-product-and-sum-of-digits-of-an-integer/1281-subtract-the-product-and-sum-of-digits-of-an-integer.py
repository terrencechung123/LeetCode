class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        list_n = [int(i) for i in str(n)] #[2,3,4]
        sum_n = sum(list_n)
        product = list_n[0]
        for j in range(1,len(list_n)):
            product =  product * list_n[j]
        return product - sum_n