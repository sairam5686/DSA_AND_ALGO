class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        vals = 0
        max_val = -float('inf')
        for i in range(len(nums)):
            if(vals + nums[i] >= 0):
                vals += nums[i]
                max_val = max(max_val , vals)
            else:
                max_val = max(max_val , nums[i])
                vals = 0
        return(max_val)
