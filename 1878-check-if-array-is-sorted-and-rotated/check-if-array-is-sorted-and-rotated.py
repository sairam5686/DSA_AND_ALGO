class Solution:
    def check(self, nums: List[int]) -> bool:
        if(len(nums) == 1):
            return True
        low , high =  0,1
        bp = 0
        dums , ind = float('inf') , 0
        for i in range(1 , len(nums)):
            if(nums[i] <  nums[i-1]):
                dums = nums[i]
                ind = i

        flag = False
        for i in range(1 , len(nums)):
            index  = (i+ ind)%len(nums)
            if(nums[index] >= nums[index-1]):
                flag = True
            else:
                return (False)
                break

        return(flag)
