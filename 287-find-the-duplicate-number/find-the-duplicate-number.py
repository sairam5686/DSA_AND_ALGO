class Solution(object):
    def findDuplicate(self, nums):
        nums.sort()
        low, high = 0 ,1
        while(high < len(nums)):
            if(nums[low] == nums[high]):
                return nums[low]

            low +=1
            high +=1  