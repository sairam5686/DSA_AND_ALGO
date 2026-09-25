class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        low , high = 0, 0
        counter = 0
        max_counter = 0
        while(high < len(nums)):
             
            if(nums[high] != 1):
                low = high+1
                counter = 0
            max_counter = max(high - low+1 , max_counter)
            high +=1
        return(max_counter)