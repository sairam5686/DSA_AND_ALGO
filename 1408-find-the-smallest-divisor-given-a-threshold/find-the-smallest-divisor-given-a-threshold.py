import math
def dev_sum(nums , divisor):
    sums = 0
    for i in nums:
        sums +=(math.ceil(float(i)/divisor))
    return  sums

class Solution(object):
    def smallestDivisor(self, nums, threshold):
        result = -1
        low , high = 1 , max(nums)
        while(low<=high):
            mid =( low + high ) // 2
            thres_checker = dev_sum(nums , mid)
            if(thres_checker<=threshold):
                result = mid
                high = mid - 1
            else:
                low = mid + 1
        return result