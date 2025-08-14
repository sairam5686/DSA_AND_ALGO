class Solution(object):
    def largestGoodInteger(self, num):
        low , high = 0 , 2
        result = None
        while(high < len(num)):
            checker = set((num[low : high + 1]))
            if(len(checker) == 1):
                result = max(result  , int(num[low:high +1]) )
            low +=1
            high +=1

        if(str(result) == '0' ):
            return("000")
        elif(result == None):
            return("")
        else:
            return(str(result))
                