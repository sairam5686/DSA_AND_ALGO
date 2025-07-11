class Solution(object):
    def removeDuplicates(self, nums):
        low ,  high = 0 ,1
        while(high <len(nums)):
            if(nums[low] != nums[high]):
                low +=1
                nums[low]  = nums[high]
            high +=1

        return(low+1)