
def solver(nums , k):
    total_hours = 0
    for i in range(len(nums)):
        total_hours += math.ceil(nums[i] / float(k))
    return total_hours

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        solution = -1
        low , high = 1 , sum(piles)
        while(low <= high):
            mid = (low + high ) // 2
            time_to_eat = solver(piles , mid)
            if(time_to_eat <= h):
                solution  = mid
                high = mid -1
            else:
                low = mid + 1
        return(solution)