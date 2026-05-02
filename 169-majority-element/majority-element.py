class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter =  1
        val = nums[0]
        for i in range( 1  , len(nums)):
            if(nums[i] == val):
                counter +=1
            else:
                if(counter == 0 ):
                    counter = 1
                    val = nums[i]
                else:
                    counter -=1
        return (val)