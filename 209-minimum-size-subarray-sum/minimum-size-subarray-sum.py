class Solution(object):
    def minSubArrayLen(self, target, nums):
        low , high = 0,0
        result =float('inf')
        dummy = 0
        while(high<len(nums)):
            dummy += nums[high]
            high += 1
            while(dummy >=target):
                dummy -= nums[low]
                low +=1
                result = min(high-low+1 , result)
          
                

        if(result == float('inf')):
            return(0)
        else:
            return(result)


                        