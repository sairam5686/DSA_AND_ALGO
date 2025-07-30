class Solution(object):
    def longestConsecutive(self, nums):
        if(len(nums) == 0):
            return( 0 )
        nums = sorted(list(set(nums)))

        checker = nums[0]
        ptr = 0
        counter = 0
        max_counter = 0
        while(ptr< len(nums)):
            if(checker == nums[ptr]):
                counter +=1
                checker +=1
                ptr +=1
            else:
                counter = 0
                checker = nums[ptr]
            max_counter = max(max_counter , counter)

        return(max_counter)