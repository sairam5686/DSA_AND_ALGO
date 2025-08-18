class Solution(object):
    def largestOddNumber(self, num):
        result = 0
        for i in range(len(num)-1 , -1, -1):
            if(num[i] == 0):
                continue
            if(int(num[i])%2 != 0):
                result = (num[:i+1])
                break
        if(result == 0):
            return ""
        return(str(result))
                        