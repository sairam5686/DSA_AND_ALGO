class Solution(object):
    def maxFrequency(self, nums, k):
        nums = sorted(nums)
        left , right = 0,0
        result = 0
        sum = 0
        while(right<len(nums)):
            sum += nums[right]
            while((nums[right]*(right-left+1))>sum+k):
                sum -=nums[left]
                left+=1
            result = max(result , right - left+1)
            right +=1
        return(result)