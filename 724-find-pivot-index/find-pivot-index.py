class Solution(object):
    def pivotIndex(self, nums):
        prefix_sums = []
        dummy = 0
        for i in range(len(nums)):
            dummy += nums[i]
            prefix_sums.append(dummy)
        print(prefix_sums)
        for i in range(len(prefix_sums)):
            if(i== 0):
                print(prefix_sums[i] , prefix_sums[len(prefix_sums)-1]- prefix_sums[i])
                if(0 == prefix_sums[len(prefix_sums)-1]- prefix_sums[i]):
                    return(i)
                    
            elif(prefix_sums[i-1] == prefix_sums[len(prefix_sums)-1]- prefix_sums[i]):
                return(i)
                
        return(-1)
                
                