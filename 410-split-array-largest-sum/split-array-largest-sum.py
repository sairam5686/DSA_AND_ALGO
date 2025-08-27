def subarray(arr , max_sum):
    counter = 1
    checker = 0
    for i in range(len(arr)):
        if(checker + arr[i] <=max_sum):
            checker += arr[i]
        else:
            counter +=1
            checker = arr[i]
    return counter

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low , high = max(nums) , sum(nums)
        result= -1
        while(low <= high):
            max_sum = (low + high)//2
            possible = subarray(nums ,max_sum)
            if(possible <= k ):
                result = max_sum
                high = max_sum -1
            else:
                low = max_sum +1
           
        return(result)
                