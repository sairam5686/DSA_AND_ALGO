def comb(row , col ):
    res = 1
    for i in range(1 , col):
        res *= row - i
        res //= i
    return res



class Solution(object):
    def generate(self, numRows):
        result_nums = [ ]
        for i in range(1 , numRows+1):
            dumbs =  []
            for j in range (1 , i+1):
                val = comb( i ,  j )
                dumbs.append(val)
            result_nums.append(dumbs)
        return (result_nums)