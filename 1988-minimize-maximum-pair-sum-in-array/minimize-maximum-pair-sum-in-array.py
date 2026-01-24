class Solution:
    def minPairSum(self, nums: List[int]) -> int:   
        nums.sort()
        low , high  = 0 , len(nums)-1
        result = min(nums)
        while(low <high):
            result = max(result , nums[low]+nums[high])
            low+=1
            high -=1
        return(result)