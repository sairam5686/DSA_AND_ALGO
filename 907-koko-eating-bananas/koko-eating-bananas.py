import math
def hours_taken(piles , eat_rate):
    total_hours = 0
    for i in range(len(piles)):
        total_hours += math.ceil(piles[i] / float(eat_rate))
    return total_hours


class Solution(object):
    def minEatingSpeed(self, piles, h):
        low , high = 1 , max(piles)
        min_solution = max(piles)
        while(low<=high ):
            mid = ((low + high)//2)
            total = hours_taken(piles,mid)
            if(total <= h):
                min_solution = mid
                high = mid -1
            else:
                low = mid + 1
                
        return min_solution