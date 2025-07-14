class Solution(object):
    def search(self, nums, target):
        flag = False
        low , high = 0 ,len(nums)-1
        while(low<=high):
            mid = (low + high )//2
            if(nums[mid]== target):
                break
            if(nums[mid] == nums[low] and nums[high] == nums[mid]):
                low +=1
                high -=1
                continue
           
            if(nums[low]<=nums[mid]):
                if(target>= nums[low] and nums[mid]>= target):
                    high = mid -1
                else:
                    low = mid + 1
            else:
                if(target>= nums[mid] and nums[high]>= target):
                    low = mid + 1
                else:
                    high = mid - 1

        if(nums[mid]== target):
            return(True)
        else:
            return(False)