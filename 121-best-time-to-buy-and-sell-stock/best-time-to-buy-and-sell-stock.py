class Solution:
    def maxProfit(self, prices: List[int]) -> int: 
        stack = [0]
        max_profit =  0
        for i in range(len(prices)-1 , -1 , -1):
            if(stack[-1]< prices[i] ):
                stack.append(prices[i])
            else:
                profit =  stack[-1] - prices[i]
                max_profit  = max(max_profit, profit)
        return(max_profit)
