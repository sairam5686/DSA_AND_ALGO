def binarysearcher(nums  , k ):
    res = 0
    for i in range(len(nums)):
        res += (math.ceil(nums[i] / k))
    return res


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low , high = 1 , max(piles)
        result  = 0
        while(low <= high):
            mid = (low + high )//2
            res = binarysearcher(piles   ,mid)
            if(res <= h  ):
                result = mid
                high = mid -1
            else:
                low = mid + 1
        return(result)