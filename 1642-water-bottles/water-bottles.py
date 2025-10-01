class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total_bottles = numBottles
        emptybottles = numBottles
        while(emptybottles >= numExchange):
            total_bottles += math.floor(emptybottles/numExchange)
            emptybottles = math.floor(emptybottles/numExchange) + (emptybottles%numExchange)
        return(total_bottles)