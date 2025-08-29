class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        low , mid , high = 0 ,1 , 2
        result = []
        while(high < len(mountain)):
            if( mountain[low]<mountain[mid] and mountain[high]< mountain[mid] ):
                result.append(mid)

            mid+=1
            high+=1
            low +=1
        return(result)
                