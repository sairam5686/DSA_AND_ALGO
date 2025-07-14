class Solution(object):
    def search(self, nums, target):
        ind = -1
        low  , high = 0, len(nums)-1
        while(low <=high):
            mid = (low + high) //2
            if(target == nums[mid]):
                
                ind = mid
                break
            elif(nums[low]<=nums[mid]):
                if(nums[mid]>= target and target>= nums[low] ):
                    high = mid-1
                else:
                    low = mid + 1
            else:
                if(nums[mid]<=target and  target <=nums[high]):
                    low = mid + 1
                else:
                    high = mid - 1

        return(ind)
                        