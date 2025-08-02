class Solution(object):
    def minCost(self, basket1, basket2):
        counter_1 = Counter(basket1)
        counter_2 = Counter(basket2)

        total_counter = counter_1+counter_2

        for i in total_counter.values():
            if(i%2 != 0 ):
                return(-1)


        misplaced = []
        for fruit , count in total_counter.items():
            mis_count = abs(count//2 - counter_1[fruit])
            misplaced.extend([fruit]*mis_count)

        misplaced.sort()
        min_cost = 0
        min_Val = min(total_counter.keys())
        for i in range(len(misplaced)//2):
            min_cost +=min(misplaced[i] , (2*min_Val))
        return(min_cost)
                