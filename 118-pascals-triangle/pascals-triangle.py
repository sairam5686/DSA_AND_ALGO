def combination(row , cols):
    result = 1
    for i in range(1 , cols):
        result *=(row - i)
        result //=i
    return result

class Solution(object):
    def generate(self, numRows):
        result = []
        for i in range(1 , numRows+1):
            dummy = []
            for j in range(1 , i+1 ):
                val = combination(i , j)
                dummy.append(val)
            result.append(dummy)
        return(result)
                