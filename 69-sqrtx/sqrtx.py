class Solution(object):
    def mySqrt(self, x):
        low , high  = 1 , x
        result = 0
        while(low <= high):
            mid = (low + high)//2
            if(mid*mid <= x):
                result = mid
                low = mid + 1
            else:
                high = mid - 1
        return result
        