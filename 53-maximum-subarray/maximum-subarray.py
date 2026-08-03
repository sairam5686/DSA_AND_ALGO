class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = max(nums)
        sum  =  0
        for i in range(len(nums)):
            sum +=nums[i]
            if(sum >=  0 ):
                max_sum= max(sum , max_sum)
            else:
                sum = 0
        return (max_sum)