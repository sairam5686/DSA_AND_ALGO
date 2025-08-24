class Solution(object):
    def longestSubarray(self, nums):
        result = 0
        if(0 not in nums):
            return(len(nums)-1)
        else:
            low , high = 0, 0
            zero_counter = 0
            while(low<=high and high<len(nums)):
                if(nums[high] ==0 ):
                    zero_counter +=1
                if(zero_counter<=1):
                    print(high , low , high-low)
                    result = max(result , (high- low))
                while(zero_counter >1):
                    if(nums[low]== 0):
                        zero_counter -=1
                    low +=1
                high +=1
        return(result)
                