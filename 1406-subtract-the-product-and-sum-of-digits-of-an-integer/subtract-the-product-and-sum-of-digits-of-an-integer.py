class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        mul_num = 1
        sum_num = 0
        n = str(n)
        for i in range(len(n)):
            mul_num *= int(n[i])
            sum_num += int(n[i])
        return(mul_num - sum_num)
                