class Solution(object):
    def minOperations(self, nums):
        low = 0
        high = 3
        counter = 0
        while(high<=len(nums)):
            while( 0 == nums[low]):
                counter +=1
                for i in range(low, high):
                    if(nums[i] == 0):
                        nums[i] = 1
                    else:
                        nums[i] = 0
            high +=1
            low+=1
            
            

        if( 0 in nums):
            return(-1)
        else:
            return(counter)