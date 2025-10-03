class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if(len(arr)<3):
            return(False)
        else:
            low ,mid , high = 0,1,2
            while(high < len(arr)):
                if(arr[low] %2 !=0 and arr[mid]%2 !=0 and arr[high]%2 != 0 ):
                    return(True)
                low +=1
                mid +=1
                high +=1
        return(False)
                