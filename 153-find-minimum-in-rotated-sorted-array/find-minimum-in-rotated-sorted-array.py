class Solution(object):
    def findMin(self, nums):
        low,high = 0,len(nums)-1
        ind = 999999
        while(low<= high):
            mid = (low + high) // 2
            print(mid)
            if(nums[low]<=nums[mid]):
                ind =min(ind ,  nums[low])
                low = mid +1

            elif(nums[high]>nums[mid]):
                ind =min( ind,nums[mid])
                high = mid-1

        return(ind)

                                