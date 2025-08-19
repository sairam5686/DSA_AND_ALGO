class Solution(object):
    def zeroFilledSubarray(self, nums):
        zeros = 0
        counts = 0
        for i in range(len(nums)):
            if(nums[i] == 0 ):
                zeros +=1
            else:
                zeros = 0
            counts +=zeros
        return(counts)
                