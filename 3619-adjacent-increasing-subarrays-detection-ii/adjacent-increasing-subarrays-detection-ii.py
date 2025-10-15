class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        prev  , inc , ans=  0, 1 ,0
        for i in range(1 , len(nums)):
            if(nums[i] > nums[i-1]):
                inc +=1
            else:
                prev = inc
                inc = 1
            ans = max(ans  , inc//2 , min(prev , inc))
        return(ans)