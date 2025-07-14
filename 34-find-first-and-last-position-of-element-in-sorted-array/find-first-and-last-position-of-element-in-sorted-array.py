class Solution(object):
    def searchRange(self, nums, target):
        low , high = 0 ,len(nums)-1
        ind = float('inf')
        if(len(nums) == 0 ):
            return([-1,-1])
        else:
            while(low<=high):
                mid  = (low+ high )//2
                if(nums[mid] == target):
                    ind = mid
                    break
                elif(nums[mid]>target ):
                    high = mid -1
                else:
                    low = mid +1


        if(ind == float('inf')):
            return([-1,-1])
        else:
            low, high = ind-1, ind+1
            while (low>=0 ):

                if(nums[low] == target):
                    low -= 1
                else:
                    break

            while (high<len(nums)):
                if(nums[high] == target):
                    high += 1
                else:
                    break
            return([low+1 , high - 1])