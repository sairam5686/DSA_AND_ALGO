class Solution(object):
    def trap(self, nums):
        l,r,lmax,rmax,total = 0,len(nums)-1,0,0,0
        while(l<r):
            if(nums[l]<=nums[r]):
                if(lmax>nums[l]):
                    total +=lmax-nums[l]
                else:
                    lmax = nums[l]
                l +=1
            else:
                if(rmax>nums[r]):
                    total +=rmax-nums[r]
                else:
                    rmax = nums[r]
                r -=1
        return(total)
                