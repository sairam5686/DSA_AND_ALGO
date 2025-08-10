class Solution(object):
    def maxConsecutive(self, bottom, top, special):
        special.sort()
        res =abs( bottom-special[0])
        low , high = 0 ,1
        while(high < len(special)):
            res = max(res , special[high]-(special[low]+1))
            high +=1
            low +=1
        res = max(res , ( top- special[-1]))
        return(res)
                