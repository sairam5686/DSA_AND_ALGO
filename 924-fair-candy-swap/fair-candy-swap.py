class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        A_sum = sum(aliceSizes)
        B_sum = sum(bobSizes)
        diff = (A_sum - B_sum) // 2
        A = set(aliceSizes)
        for B in set(bobSizes):
            if(diff+B in A):
                return([diff+B , B])