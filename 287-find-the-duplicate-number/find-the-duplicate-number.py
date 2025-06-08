class Solution(object):
    def findDuplicate(self, nums):
        low , high = 0,0
        low2 = 0
        while(True):
            low = nums[low]
            high = nums[nums[high]]
            if(low == high):
                break
            
        while(True):
            low = nums[low]
            low2 = nums[low2]
            if(low ==low2):
                break
        return low  