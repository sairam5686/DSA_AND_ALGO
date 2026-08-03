def is_sorted(arr):
    low , high = 0 , 1
    while(high< len(arr)):
        if(arr[low] > arr[high]):
            return (False , high)
        low +=1
        high +=1

    return (True , None)



class Solution:
    def check(self, nums: List[int]) -> bool:    
        flag , val = is_sorted(nums)
        if(flag==True):
            return (True)
        else:
            first_half  , last_half =nums[:val] , nums[val:]
            last_half.extend(first_half)
            res , val = is_sorted(last_half)
            if(res == True):
                return (True)
            else:
                return(False)

