class Solution(object):
    def findPeakElement(self, nums):
        ptr = 1
        res = 0
        if(len(nums)==2 and nums[1]>nums[0]):
            return 1
        if(nums[len(nums)-1] >nums[len(nums)-2]):
            return len(nums)-1
        while(ptr <= len(nums)-2):
            print(nums[ptr-1] , nums[ptr] ,nums[ptr+1])
            if(nums[(ptr-1)]<nums[ptr]>nums[ptr+1]):
                res = ptr
                break
            ptr +=1

        return(res)