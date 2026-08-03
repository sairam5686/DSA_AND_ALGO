class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_element = -1
        temp = [-1]*len(prices)
        for i in range(len(prices)-1  , -1 , -1):
            max_element = max(prices[i] , max_element )
            temp[i] = max_element
        result =  0
        for i in range(len(prices)):
            result = max(temp[i] - prices[i]  , result)
        return (result)