
def isSorted(num):
    for i in range( 1, len(num)):
        if( num[i-1]> num[i]):
            return False , i
    return True , None


class Solution:
    def check(self, nums: List[int]) -> bool:    
        low , high =  0 , 1
        sort_flag , rotate_flag  = False , False
        flag , val = isSorted(nums)
        if (flag):
            return(True)
        else:
            start ,end =nums[val:] , nums[:val]
            start.extend(end)
            flag,val  = isSorted(start)
            if(flag):
                return(True)
            else:
                return(False)