class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter  , max_counter = 0 ,  0 
        for i in range(len(nums)):
            if(nums[i] == 1):
                counter +=1
            else:
                counter = 0
            max_counter = max(max_counter , counter)

        max_counter = max(counter , max_counter)
        return(max_counter)