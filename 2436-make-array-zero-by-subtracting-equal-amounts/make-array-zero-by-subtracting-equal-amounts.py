class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        counter = 0
        nums = list(set(nums))
        for i in range(len(nums)):
            if(nums[i] != 0 ):
                counter +=1
        return counter