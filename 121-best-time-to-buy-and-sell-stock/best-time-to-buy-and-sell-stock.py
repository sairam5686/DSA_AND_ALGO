class Solution(object):
    def maxProfit(self, nums):
        stack  = [0]
        max_profit =   0 
        for i in range(len(nums)-1 , -1 , -1):
            if(stack[-1] < nums[i]):
                stack.append(nums[i])
            else:
                profit = stack[-1] - nums[i]
                max_profit = max(profit  , max_profit)
        return max_profit