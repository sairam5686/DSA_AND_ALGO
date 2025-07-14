class Solution(object):
    def searchRange(self, nums, target):
        ind =-1
        low , high = 0 , len(nums)-1
        while(low <= high):
            mid = (low + high) // 2
            if(nums[mid] == target):
                ind = mid
                high = mid -1
            elif(nums[mid]>target):
                high = mid -1
            else:
                low = mid + 1

        ind2 =-1
        low , high = 0 , len(nums)-1
        while(low <= high):
            mid = (low + high) // 2
            if(nums[mid] == target):
                ind2 = mid
                low = mid +1
            elif(nums[mid]>target):
                high = mid -1
            else:
                low = mid + 1
        return([ind, ind2])
