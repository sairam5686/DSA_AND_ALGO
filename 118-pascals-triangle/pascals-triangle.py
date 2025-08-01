def combination(row , col):
    res = 1
    for i in range(1,col):
        res *= (row - i )
        res //=i
    return res



class Solution(object):
    def generate(self, numRows):
        result = []
        for i in range(1, numRows+1):
            dummy = []
            for j in range(1 , i+1):
                dummy.append(combination(i , j))
            result.append(dummy)
        return(result)

                

            