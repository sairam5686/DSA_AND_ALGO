class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        emptybottle = numBottles
        total_bottle = numBottles
        bottle_counter = 0
        while(emptybottle >= numExchange):
            # print(emptybottle , numExchange , total_bottle)
            emptybottle = emptybottle - numExchange
            emptybottle +=1
            total_bottle +=1
            numExchange +=1
        
        return(total_bottle)
                