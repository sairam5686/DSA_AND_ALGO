class Solution(object):
    def maxSubArray(self, nums):
        ptr =  0
        val = 0

        result = max(nums)
        while(ptr < len(nums)):
            val += nums[ptr]
            result = max(val , result)
            if(val < 0 ):
                val = 0
            ptr +=1
        return (result)