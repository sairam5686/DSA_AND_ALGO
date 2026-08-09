class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = max(nums)
        temp_sum = 0
        for i in range(0 , len(nums)):
            if((temp_sum + nums[i])  >=  0 ):
                temp_sum += nums[i]
                max_sum = max(max_sum  , temp_sum)
            else:
                temp_sum = 0
        return (max_sum)