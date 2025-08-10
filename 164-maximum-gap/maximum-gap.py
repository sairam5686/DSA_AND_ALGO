class Solution(object):
    def maximumGap(self, nums):
        nums = sorted(nums)
        res = 0
        low,high = 0 ,1
        if(len(nums)>1):
            while(high<len(nums)):
                res = max(res , nums[high] - nums[low])
                low +=1
                high +=1
            return(res)
        else:
            return(0)
                