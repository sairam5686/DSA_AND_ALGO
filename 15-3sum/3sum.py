class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        res = []
        for i in range(0,len(nums)):
            low = i+1
            high = len(nums)-1
            while(low<high):
                if(nums[i]+nums[low]+nums[high] >0):
                    high -=1
                elif(nums[i]+nums[low]+nums[high] <0):
                    low +=1
                else:
                        if([nums[i],nums[low],nums[high]] not in res):
                            res.append([nums[i],nums[low],nums[high]])
                        low +=1
                        high -=1
        return(res)
                