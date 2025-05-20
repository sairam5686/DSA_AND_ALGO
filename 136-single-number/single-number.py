class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        for i in range(0,len(nums)):
            sum ^=nums[i]
        return(sum)
                