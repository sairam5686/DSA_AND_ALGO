class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        low , high = 0  , len(nums)-1
        solution = -1
        while(low <= high):
            mid = (low + high )//2

            
            if(nums[mid] == target  ):
                return True
            elif(nums[low] == nums[mid] and nums[high] == nums[low]):
                high -=1
                low +=1
            elif(nums[low] <= nums[mid]):
                if(nums[low] <= target and nums[mid] >= target ):
                    high = mid -1
                else:
                    low = mid + 1
            else:
                if(nums[mid] <= target and nums[high] >= target):
                    low = mid +1
                else:
                    high = mid - 1
        
        return False