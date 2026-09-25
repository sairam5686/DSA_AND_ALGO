class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        low , high = 0 , 0
        while(high < len(nums)):
                if(nums[low] != nums[high]):
                    low +=1
                    nums[low] , nums[high] = nums[high] , nums[low ]
                high +=1
        return (low+1 )
