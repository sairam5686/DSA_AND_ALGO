class Solution(object):
    def subarraySum(self, nums):   
        prefix_sum = []
        dummy = 0
        for i in range(len(nums)):
            dummy += nums[i]
            prefix_sum.append(dummy)
        print(prefix_sum)

        result = 0
        for i in range( len(nums)):
            start = max(0  , i - nums[i])
            end = i
            if(start == 0 ):
                result +=(prefix_sum[end])
            else:
                result += (prefix_sum[end] - prefix_sum[start-1])
        return(result)
                